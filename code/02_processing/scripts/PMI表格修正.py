import pandas as pd

# 1. 輔助函數：格式化數字
def format_number(val) -> str:
    if pd.isna(val):
        return "未知"
    try:
        f_val = float(val)
        if f_val % 1 == 0:
            return str(int(f_val))
        return str(f_val)
    except ValueError:
        return str(val)

# 2. 型號組裝函數
def build_model(row: pd.Series) -> str:
    diameter = row.get('公稱 外徑')
    lead = row.get('導程')
    C = row.get('珠卷數')
    return f"{format_number(diameter)}-{format_number(lead)}-C{format_number(C)}"

# 3. 語意文本生成函數
def build_semantic_text(row: pd.Series) -> str:
    columns = ["系列", "Source_Page", "型號", "公稱 外徑", "導程", "珠徑", "珠卷數", "動負荷 C (kfg)", "靜負荷 Co (kfg)", "剛性 kfg/umk"]
    return (
        f"這是銀泰 (PMI) 的滾珠螺桿規格。系列名稱為 {row.get(columns[0], '未知')}，"
        f"型號為 {row.get(columns[2], '未知')}。外徑為 {format_number(row.get('公稱 外徑'))} mm，"
        f"導程為 {format_number(row.get('導程'))} mm，鋼珠直徑為 {format_number(row.get("珠徑"))} mm，"
        f"珠卷數為 {row.get(columns[6], '未知')}，"
        f"動負荷為 {format_number(row.get(columns[7]))} kgf，靜負荷為 {format_number(row.get(columns[8]))} kgf，"
        f"剛性為 {format_number(row.get(columns[9]))} kgf/um。"
    )

def main():
    file_path = r"C:\Users\e11338\Desktop\Feed System GAI\data\PMI_Optimized_Core.xlsx"
    print(f"正在讀取檔案: {file_path}")
    
    # 讀取檔案
    df = pd.read_excel(file_path, engine='openpyxl')
    
    # === 直接在原有的 DataFrame 上進行修改與擴充 ===
    
    # 步驟 A：強制覆寫「型號」欄位 (如果原本沒有這個欄位，Pandas 會自動新增)
    print("正在依據規則 (外徑-導程) 重新組裝「型號」...")
    df["型號"] = df.apply(build_model, axis=1)
    
    # 步驟 B：生成或覆寫 semantic_text 欄位
    print("正在生成 semantic_text...")
    df["semantic_text"] = df.apply(build_semantic_text, axis=1)
    
    # ===============================================
    
    # 移除原本的 columns 過濾機制！
    # 現在 df 包含了你原本 Excel 的所有欄位，加上更新後的「型號」與「semantic_text」
    
    output_path = r"C:\Users\e11338\Desktop\Feed System GAI\data\PMI_Optimized_Core_v2.xlsx"
    
    # 直接將完整資料匯出
    df.to_excel(output_path, index=False, engine='openpyxl')
    print(f"✅ 處理完成！原始數據已保留，並成功匯出至: {output_path}")

if __name__ == "__main__":
    main()