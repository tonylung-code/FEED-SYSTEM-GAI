### 指定輸入參數
maximum_feed_rate = 48000 #最大進給速率, mm/min
motor_max_speed = 3000 #馬達最高轉速，預設3000 rpm
acceleration = "" #加速度
reduction_ratio = 1 #減速比
load = 775 #負載
cutting_force = 343 #切削力
length = 924 # 行程
preload_rate = 0.05 #預壓率
axis = ["x", "y", "z"]
gravity_axis_YN = True #判斷重力軸
support_type = "fixed_supported" #支撐類型["supported_supported", "fixed_supported", "fixed_fixed", "fixed_free"]
combination = "DF" #軸承組合類型 ["DF", "DFD", "DFF"]


from math import pi
import math
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.unicode.ambiguous_as_wide', True)

hiwin_df = pd.read_excel(r"C:\Users\e11338\Desktop\Feed System GAI\data\HIWIN_Final_Data_V1.xlsx", engine='openpyxl')
pmi_df = pd.read_excel(r"C:\Users\e11338\Desktop\Feed System GAI\data\PMI_Optimized_Core_v2.xlsx", engine='openpyxl')

def Guide_list():
    hiwin_df = pd.read_excel(r"C:\Users\e11338\Desktop\Feed System GAI\data\HIWIN_Final_Data_V1.xlsx", engine='openpyxl')
    pmi_df = pd.read_excel(r"C:\Users\e11338\Desktop\Feed System GAI\data\PMI_Optimized_Core_v2.xlsx", engine='openpyxl')
    hiwin_guides = hiwin_df["導程"].unique().tolist()
    pmi_guides = pmi_df["導程"].unique().tolist()
    result = list(set(hiwin_guides) | set(pmi_guides))
    print(f"HIWIN導程選項: {hiwin_guides}")
    print(f"PMI導程選項: {pmi_guides}")
    print(result)

def Diameter_list():
    hiwin_df = pd.read_excel(r"C:\Users\e11338\Desktop\Feed System GAI\data\HIWIN_Final_Data_V1.xlsx", engine='openpyxl')
    pmi_df = pd.read_excel(r"C:\Users\e11338\Desktop\Feed System GAI\data\PMI_Optimized_Core_v2.xlsx", engine='openpyxl')
    hiwin_guides = hiwin_df["公稱 外徑"].unique().tolist()
    pmi_guides = pmi_df["公稱 外徑"].unique().tolist()
    result = list(set(hiwin_guides) | set(pmi_guides))
    print(f"HIWIN公稱外徑選項: {hiwin_guides}")
    print(f"PMI公稱外徑選項: {pmi_guides}")
    print(result)


# 導程 & 最大轉速，最大進給速率 = 導程 * 最大轉速 * 減速比
def Guide_calculation(maximum_feed_rate, motor_max_speed, reduction_ratio):
    guide = maximum_feed_rate / (motor_max_speed * reduction_ratio) #導程
    guide_list = [2.5, 2.54, 4.0, 5.0, 6.0, 2.0, 8.0, 5.08, 10.0, 3, 12.0, 15.0, 16.0, 20.0, 24, 25.0, 30.0, 32.0, 35.0, 36.0, 40.0, 50.0, 60]
    guide_f = min(guide_list, key=lambda x: abs(x - guide))
    #print(f"計算出的導程: {guide}mm, 最接近的導程選項: {guide_f}mm")

    return guide_f
#guide = Guide_calculation(maximum_feed_rate, motor_max_speed, reduction_ratio)

#直徑計算
def Diameter_calculation(gravity_axis_YN, load, cutting_force, length, maximum_feed_rate, guide, support_type):
    support_factors = {
        "supported_supported": {"f": 9.7, "N": 1.0},
        "fixed_supported": {"f": 15.1, "N": 2.0},
        "fixed_fixed": {"f": 21.9, "N": 4.0},
        "fixed_free": {"f": 3.4, "N": 0.25}
    }
    
    f_val = support_factors[support_type]["f"]
    N_val = support_factors[support_type]["N"]
    
    Nm = (maximum_feed_rate / guide) #臨界轉速(螺桿轉速)

    #由導螺桿臨界轉速(DmN)估算導螺桿桿徑
    #安全係數 (α = 0.8)
    dr_n = math.ceil((Nm * length**2) / (0.8 * f_val * (10**7)))# dr = (n * (length**2) / f) * (10**-7)
  
    #由挫曲負荷估算導螺桿桿徑
    if gravity_axis_YN:
        p = (load + cutting_force) * 2
    else:
       cof = 0.008 #摩擦力係數
       ff = load * cof 
       p = (cutting_force + ff) * 2
    E = 21000 #kgf/mm2
    dr_p =  math.ceil((p * 64 * (length**2) / (N_val * (pi**3) * E))**0.25)

    #拉伸負荷估算導螺桿桿徑
    allowable_stress = 14.7 
    #因負載 p*2 ，在拉伸公式中已有安全係數，則 p*0.5 修正回來
    dr_t =  math.ceil(math.sqrt((4 * (p *0.5)) / (math.pi * allowable_stress))) 
    
    #取大值
    #print(f"由挫曲負荷估算導螺桿桿徑: {dr_p}mm, 由導螺桿臨界轉速估算導螺桿桿徑: {dr_n}mm, 由拉伸負荷估算導螺桿桿徑: {dr_t}mm")
    dr_F =  max(dr_n, dr_p, dr_t)
    dr_F = dr_F + 4

    #由DN估算導螺桿桿徑
    dr_DN = round(150000 / Nm, 0)
    #print(f"直徑下限: {dr_F}mm, 直徑上限: {dr_DN}mm")
    #print(f"{dr_F}mm < 螺桿直徑 < {dr_DN}mm")

    d_list = [8, 10, 12, 14, 15, 16, 20, 25, 28, 32, 36, 38, 40, 45, 50, 55, 60, 63, 70, 80, 100]
    suitable_dr = []
    last_idx = 0
    found_any = False
    for diameter in range(len(d_list)):
        # 同時符合強度要求 (dr_F) 且在轉速限制內 (dr_DN)
        
        current_d = d_list[diameter]

        # 1. 使用 Pythonic 的連續比較語法
        if dr_F <= current_d <= dr_DN:
            suitable_dr.append(current_d)
            last_idx = diameter

    #suitable_dr.extend(d_list[last_idx + 1 : last_idx + 4])

    #print(suitable_dr)

    #print("="*100)
    #print(f"導程: {guide}")
    #print("="*100)
    return dr_F, dr_DN, suitable_dr, p, dr_t
#dr_F, dr_DN, suitable_dr, p, dr_t = Diameter_calculation(gravity_axis_YN, load, cutting_force, length, maximum_feed_rate, guide, support_type)

#動負荷計算
def C_calculation(cutting_force, load, gravity_axis_YN, preload_rate):
    
    if gravity_axis_YN:
            p = (load + cutting_force)
    else:
        cof = 0.008 #摩擦力係數
        ff = load * cof 
        p = (cutting_force + ff)

    c = round(p / 3 / preload_rate, 0)
    #print(f"動負荷: {c} kfg")  
    return c
#c = C_calculation(cutting_force, load, gravity_axis_YN, preload_rate)

# 算出直徑的推薦值後使用型錄中有的值徑算出實際挫曲負荷及臨界轉速，驗證
def verify_ballscrew_safety(dr_F, length, support_type="fixed_supported"):
    dr = dr_F - 4
    support_factors = {
        "supported_supported": {"f": 9.7, "N": 1.0},
        "fixed_supported": {"f": 15.1, "N": 2.0},
        "fixed_fixed": {"f": 21.9, "N": 4.0},
        "fixed_free": {"f": 3.4, "N": 0.25}
    }
    
    f_val = support_factors[support_type]["f"]
    N_val = support_factors[support_type]["N"]

    # --- 反推 1：容許臨界轉速 (rpm) ---
    # 依據通用/PMI公式，並乘上安全係數 0.8
    allowable_speed = round(0.8 * (f_val * dr * (10**7)) / (length ** 2), 2)

    # --- 反推 2：容許最大壓縮力/挫曲負荷 (kgf) ---
    # 依據尤拉公式推導，安全係數 alpha 取 0.5
    E = 21000
    alpha = 0.5
    I = (math.pi * (dr ** 4)) / 64
    allowable_buckling = round(alpha * (N_val * (math.pi ** 2) * E * I) / (length ** 2), 2)

    # --- 反推 3：容許最大拉伸力 (kgf) ---
    # 依據應力公式推導
    allowable_stress = 14.7
    A = (math.pi * (dr ** 2)) / 4
    allowable_tensile = round(allowable_stress * A, 2)

    # print(f"公稱外徑_mm: {dr_F}")
    # print(f"容許臨界轉速_rpm: {round(allowable_speed, 2)}")
    # print(f"容許最大壓縮力(挫曲)_kgf: {round(allowable_buckling, 2)}")
    # print(f"容許最大拉伸力_kgf: {round(allowable_tensile, 2)}")
    # print("="*100)
    return allowable_speed, allowable_buckling, allowable_tensile
#allowable_speed, allowable_buckling, allowable_tensile = verify_ballscrew_safety(dr_F, length, support_type="fixed_supported")

from typing import List, Dict, Any
#型號比對
def Model_lookup(hiwin_df, pmi_df, suitable_dr, guide, c):
    """
    根據計算出的參數，於 HIWIN 與 PMI 資料庫中查找最佳滾珠螺桿型號。
    
    :param hiwin_df: HIWIN 螺桿型錄 DataFrame
    :param pmi_df: PMI 螺桿型錄 DataFrame
    :param suitable_dr: 容許的公稱直徑清單 (例如: [25, 32])
    :param guide: 目標導程
    :param c: 最低要求之動負荷
    :return: 包含兩品牌推薦結果的 Dictionary
    """

    def _search_logic(df: pd.DataFrame, brand_name: str) -> Any:
        """內部搜尋邏輯，確保程式碼不重複 (DRY 原則)"""
        if df.empty:
            return f"{brand_name} 資料庫為空"
            
        # 1. 取得該品牌可用導程，依距離排序並取前 4 名
        available_guides = sorted(df["導程"].unique(), key=lambda x: abs(x - guide))
        search_guides = available_guides[:4]
        
        # 2. 階層搜尋 (布林遮罩扁平化)
        for current_g in search_guides:
            mask = (
                (df["導程"] == current_g) & 
                (df["公稱 外徑"].isin(suitable_dr)) & 
                (df["動負荷 C (kfg)"] >= c)
            )
            
            matched_df = df[mask]
            
            if not matched_df.empty:
                # 1. 導程 (由低到高 -> True)
                # 2. 公稱 外徑 (由低到高 -> True)
                # 3. 動負荷 C (kfg) (由高到低 -> False)
                sorted_df = matched_df.sort_values(
                    by=["導程", "公稱 外徑", "動負荷 C (kfg)"], 
                    ascending=[True, True, False]
                )
                
                # 定義輸出的欄位清單
                target_cols = ["系列", "型號", "公稱 外徑", "導程", "動負荷 C (kfg)", "剛性 kfg/umk"]
                
                # 確保要求的欄位真的存在於 Excel 中
                valid_cols = [col for col in target_cols if col in sorted_df.columns]

                return sorted_df[valid_cols]
            
        clean_guides = [int(g) if g % 1 == 0 else round(float(g), 1) for g in search_guides]

        return f"在最接近的導程 {clean_guides} 中，無符合外徑與動負荷條件之規格"


    # 執行比對並組裝結果
    results = {
        "HIWIN": _search_logic(hiwin_df, "HIWIN"),
        "PMI": _search_logic(pmi_df, "PMI")
    }
    
    return results

#計算剛性
#螺桿剛性-1 + 軸承剛性-1 + 螺帽剛性-1
#軸承內徑為型號前兩位數字，設定值為螺桿值徑-10 取最接近值

def Rigidity_calculation(recommended_dict, length, combination):

    """
    針對查詢結果字典中的每一支螺桿，計算總剛性並新增至表格中。
    
    :param recommended_dict: Model_lookup 產出的結果字典 {"HIWIN": df, "PMI": df}
    :param bearing_df: 軸承資料庫 DataFrame
    :param length: 螺桿無負荷長度 (mm)
    :param combination: 軸承排列方式 ("DF", "DFD", "DFF")
    """

    K_bearing = {
    "品牌": ["NSK", "NSK", "NSK", "NSK", "NSK", "NSK", "NSK","NSK", "NSK","NSK", "NSK", "NSK", "NSK"],
    "型號": ["17TAC 47B", "20TAC 47B", "25TAC 62B", "30TAC 62B", "35TAC 72B", "40TAC 72B", "40TAC 90B","45TAC 75B", "45TAC 100B","50TAC 100B", "55TAC 100B", "55TAC 120B", "60TAC 120B"],
    "內徑_mm": [17, 20, 25, 30, 35, 40, 40, 45, 45, 50, 55, 55, 60],
    "剛性_DF_N/um": [750, 750, 1000, 1030, 1180, 1230, 1320, 1270 ,1520, 1570, 1570, 1760, 1760], 
    "剛性_DFD_N/um": [1080, 1080, 1470, 1520, 1710, 1810, 1960, 1910, 2210, 2300, 2300, 2650, 2650],
    "剛性_DFF_N/um": [1470, 1470, 1960, 2010, 2350, 2400, 2650, 2550, 3000, 3100, 3100, 3550, 3550]
    }
    K_bearing_df = pd.DataFrame(K_bearing)
    # print(K_bearing_df.to_markdown())
    # 1. 估算根徑 (公稱外徑 - 粗估鋼珠直徑4mm)
    def calc_single_row(row):
        D = row["公稱 外徑"]
        catalog_K = row["剛性 kfg/umk"]  # 單位: kgf/um
        dr = D - 4

        #螺桿軸剛性 Ks
        # 參考上銀公式 M36
        K_s = 16.8 * (dr ** 2) / length

        #螺帽實際剛性
        # 參考上銀公式 M38 / 銀泰規範
        K_n = 0.8 * catalog_K

        # 支撐軸承剛性 Kb (常數預設)
        d = dr - 10
        db = min(K_bearing_df["內徑_mm"].unique(), key=lambda x: abs(x - d))
        col_name = f"剛性_{combination}_N/um"
        K_b_N_um = K_bearing_df[K_bearing_df["內徑_mm"] == db][col_name].values[0]
        
        K_b = K_b_N_um/9.81
        #總剛性計算
        K_total = round(1 / (1/K_s + 1/K_n + 1/K_b), 2)
        return K_total 
    
    for brand, df in recommended_dict.items():
        if isinstance(df, pd.DataFrame) and not df.empty:
            # 將計算結果新增為一個新欄位
            df["總剛性 (kgf/um)"] = df.apply(calc_single_row, axis=1)
            
    return recommended_dict
#馬達扭矩計算
def Motor_torque_calculation(guide, load, cutting_force):
    w2 = load
    hsp = guide
    cof = 0.008
    me = 0.9
    Tt1 = (1 + cof) * hsp * w2 / (2 * pi * me) #kgf*mm
    Tt2 = abs((1 - cof) * hsp * w2 / (2 * pi * me)) #kgf*mm
    Tt = round(max(Tt1, Tt2) * 9.8 * 1e-3, 2) #N*m
    
    fc = cutting_force
    Tc = round((fc * hsp * me) / (2*pi)* 9.8 * 1e-3, 2) #N*m

    Trf = Tc + Tt
    # print(f"移動件所引起的摩擦扭矩: {Tt} N．mm, 軸向力引起的扭矩:{Tc} N．mm")
    # print(f"外加負荷引起之扭矩: {Trf} N．mm")
    return Trf

#馬達慣量計算
def Motor_inertia_calculation(length, suitable_dr, load, guide):
    proportion = 0.0078
    L = length
    g = 980
    Js_raw = pi * proportion * (L* 0.1 )* ((suitable_dr[-1]*0.1)**4) / (32* g ) # kgf*cm*s**2
    W = load
    hsp = guide * 0.1
    Jt_raw = W / g * (hsp / 2 / math.pi)**2 #增加減速比考慮
    Js_motor = Js_raw * (reduction_ratio ** 2)
    Jt_motor = Jt_raw * (reduction_ratio ** 2)
    JL = round(Js_motor + Jt_motor, 4)
    # print(f"公稱外徑_mm: {suitable_dr[-1]}")
    # print(f"負載慣量: {JL} kgf．cm．s2")
    # print("=" *100)
    return JL
# Trf = Motor_torque_calculation(guide, load, cutting_force)
# JL = Motor_inertia_calculation(length, suitable_dr, load, guide)

# print()
# print()

def run_ballscrew_calculation(params: dict) -> dict:
    """
    接收來自 UI 的參數，執行所有計算，並回傳結果字典。
    """
    # 從傳入的字典解析參數 (並給予安全預設值)
    maximum_feed_rate = params.get("maximum_feed_rate", 48000)
    motor_max_speed = params.get("motor_max_speed", 3000)
    reduction_ratio = params.get("reduction_ratio", 1)
    load = params.get("load", 775)
    cutting_force = params.get("cutting_force", 343)
    length = params.get("length", 924)
    preload_rate = params.get("preload_rate", 0.05)
    gravity_axis_YN = params.get("gravity_axis_YN", True)
    support_type = params.get("support_type", "fixed_supported")
    combination = params.get("combination", "DF")

    # 把原本散落在全域的計算，全部移到這裡面執行
    guide = Guide_calculation(maximum_feed_rate, motor_max_speed, reduction_ratio)
    dr_F, dr_DN, suitable_dr, p, dr_t = Diameter_calculation(gravity_axis_YN, load, cutting_force, length, maximum_feed_rate, guide, support_type)
    c = C_calculation(cutting_force, load, gravity_axis_YN, preload_rate)
    
    allowable_speed, allowable_buckling, allowable_tensile = verify_ballscrew_safety(dr_F, length, support_type)
    
    # 執行比對與剛性計算 (這是您原本 main 裡面做的事)
    results = Model_lookup(hiwin_df, pmi_df, suitable_dr, guide, c)
    final_results = Rigidity_calculation(results, length, combination)
    
    Trf = Motor_torque_calculation(guide, load, cutting_force)
    JL = Motor_inertia_calculation(length, suitable_dr, load, guide)

    # 將所有需要的結果打包回傳給 Streamlit
    return {
        "guide": guide,
        "dynamic_load": c,
        "torque": Trf,
        "inertia": JL,
        "allowable_speed": allowable_speed,
        "allowable_buckling": allowable_buckling,
        "allowable_tensile": allowable_tensile,
        "recommendations": final_results # 包含 HIWIN 與 PMI 的 DataFrame
    }


if __name__ == "__main__":
    test_params = {
        "maximum_feed_rate": 48000,
        "motor_max_speed": 3000,
        "reduction_ratio": 1,
        "load": 775,
        "cutting_force": 343,
        "length": 924,
        "preload_rate": 0.05,
        "gravity_axis_YN": True,
        "support_type": "fixed_supported",
        "combination": "DF"
    }
    # 測試呼叫
    print("--- 開始本地端測試 ---")
    output = run_ballscrew_calculation(test_params)
    
    print("\n螺桿推薦型號:")
    for brand, result in output["recommendations"].items():
        print(f"\n[{brand}]")
        if isinstance(result, pd.DataFrame):
            print(result.to_string(index=False))
        else:
            print(result)
    print("=" * 100)