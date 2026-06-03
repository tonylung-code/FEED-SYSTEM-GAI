import fitz
import os
from pathlib import Path
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# 初始化模型
model = SentenceTransformer('BAAI/bge-m3')

# 提取指定頁數範圍內的圖片及轉存json
# 處理伺服馬達仕樣檔案圖片擷取
def pdf_to_images_basic(pdf_name):
    # 指定內容頁數
    start_page=32
    end_page=130

    # 創建資料夾
    title='characteristics_curves_and_data_sheet' 
    folder_path = Path(os.path.abspath(f"./{pdf_name}/{title}"))
    folder_path.mkdir(parents=True, exist_ok=True)
    
    # 打開pdf文件檔
    doc = fitz.open(f"{pdf_name}.pdf")
    
    # 儲存
    result_dict={}
    result_list = []
    
    for page_num in range(start_page, end_page):
        dict = {}
        # 移除結構樹問題
        catalog_xref = doc.pdf_catalog()
        doc.xref_set_key(catalog_xref, "StructTreeRoot", "null")
        # 提取圖片標題
        doc[page_num].set_cropbox(fitz.Rect(50, 50, 565, 150))
        text = doc[page_num].get_text()
        lines_array = text.split('\n')
        lines_array = [line.strip() for line in lines_array if line.strip()]

        # 存到字典
        dict[page_num] = lines_array # 存頁數+內容
        result_list.append(dict)

        if(len(lines_array)>3):
            # 將當前頁面轉換為圖片(有標題部分)
            doc[page_num].set_cropbox(fitz.Rect(50, 100, 565, 340))
            pix = doc[page_num].get_pixmap()
            pix.save(f"{pdf_name}\\characteristics_curves_and_data_sheet\\page_{page_num}.png")    
        else:
            # 將當前頁面轉換為圖片(沒有標題)
            doc[page_num].set_cropbox(fitz.Rect(50, 50, 565, 300))
            pix = doc[page_num].get_pixmap()
            pix.save(f"{pdf_name}\\characteristics_curves_and_data_sheet\\page_{page_num}.png")

    result_dict[title]=result_list # 存標題+內容

    # 儲存成json檔
    with open(f"{pdf_name}.json", 'w', encoding='utf-8') as f:
        json.dump(result_dict, f, ensure_ascii=False, indent=2)
    print(f"✓ 已保存到: {pdf_name}.json")

    print(f"轉換完成！共有 {len(result_list)} 張圖片")    
    doc.close()

# 將json檔轉換成陣列
def json_to_units(json_path):

    # 打開json檔
    with open(json_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    
    units = []
    
    # 打開json檔結構
    for title, pages_list in json_data.items():
        # pages_list 是一個列表，包含多個字典
        for page_dict in pages_list:
            for page_num, contents in page_dict.items():
                # ["大標題", "頁碼", "內容1", "內容2", ...]
                unit = [title, page_num] + contents
                units.append(unit)
    
    print(f"✓ JSON轉換完成，共生成 {len(units)} 個單元")
    """
    # 顯示前三個元素確認
    for i, unit in enumerate(units[:3]):
        print(f"  示例{i+1}: {unit}")
    """
    return units

# 保存向量模型
def units_to_vectors_and_save(json_file):

    # 得到json跟npz檔名
    npz_file = json_file.replace('.json', '.npz')
    # 取得陣列
    units = json_to_units(json_file)

    # 將陣列組合成文本
    unit_texts = []
    for unit in units:
        text = ' '.join(unit)
        unit_texts.append(text)
    
    # 生成向量
    vectors = model.encode(unit_texts, normalize_embeddings=True)
    print(f"✓ 向量完成: {vectors.shape}")
    
    # 保存模型
    units_serialized = np.array(units, dtype=object)
    np.savez_compressed(
        npz_file,
        vectors=vectors,
        units=units_serialized,
        metadata=np.array([{
            'model': 'BAAI/bge-m3',
            'vector_shape': vectors.shape,
            'num_units': len(units),
            'embedding_dimension': vectors.shape[1]
        }], dtype=object)
    )
    
    print(f"✓ 已保存到: {npz_file}")
    return vectors, units

# 將手冊的json轉為向量模型
def embeddings_bgem3(json_name):

    # 1. 載入json檔
    with open(json_name, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 2. 提取所有content字段
    contents = [item['content'] for item in data if 'content' in item]
    print(f"共提取 {len(contents)} 則内容")

    # 3. 生成向量
    embeddings = model.encode(
        contents,
        batch_size=32,          
        show_progress_bar=True,
        normalize_embeddings=True 
    )

    # 4. 保存為.npz格式
    output_path =  json_name.replace('.json', '.npz')
    np.savez_compressed(
        output_path,
        embeddings=embeddings,
        texts=np.array(contents, dtype=object)  # 保存原文便於追溯
    )

    print(f"向量已保存至: {output_path}")
    loaded = np.load(output_path, allow_pickle=True)
    print(f"向量形状: {loaded['embeddings'].shape}, 文本数量: {len(loaded['texts'])}")

if __name__ == '__main__':
    # (1)擷取圖片並轉換成json檔跟向量檔
    name = "B65542EN_01_ai-D伺服馬達仕樣"
    pdf_to_images_basic(name)
    vectors, units = units_to_vectors_and_save(f"{name}.json")

    # (2)手冊json檔轉換成向量檔
    json_files = ['FANUC_final_chunks.json', 'HIWIN_final_chunks.json', 'PMI_final_chunks.json']
    for json_file in json_files:
        embeddings_bgem3(json_file)