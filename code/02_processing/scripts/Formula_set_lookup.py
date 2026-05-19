### 指定輸入參數
maximum_feed_rate = 48000 #最大進給速率, mm/min
motor_max_speed = 4000 #馬達最高轉速，預設3000 rpm
acceleration = "" #加速度
reduction_ratio = 1 #減速比
load = 775 #負載
cutting_force = 343 #切削力
length = 924 # 行程
preload_rate = 0.05 #預壓率
axis = ["x", "y", "z"]
gravity_axis_YN = True #判斷重力軸
support_type = "fixed_supported" #支撐類型

from math import pi
import math
import pandas as pd

def Guide_list():
    hiwin_df = pd.read_excel(r"C:\Users\e11338\Desktop\Feed System GAI\data\HIWIN_Final_Data_V1.xlsx", engine='openpyxl')
    pmi_df = pd.read_excel(r"C:\Users\e11338\Desktop\Feed System GAI\data\PMI_Optimized_Core.xlsx", engine='openpyxl')
    hiwin_guides = hiwin_df["導程"].unique().tolist()
    pmi_guides = pmi_df["導程"].unique().tolist()
    result = list(set(hiwin_guides) | set(pmi_guides))
    print(f"HIWIN導程選項: {hiwin_guides}")
    print(f"PMI導程選項: {pmi_guides}")
    print(result)

def Diameter_list():
    hiwin_df = pd.read_excel(r"C:\Users\e11338\Desktop\Feed System GAI\data\HIWIN_Final_Data_V1.xlsx", engine='openpyxl')
    pmi_df = pd.read_excel(r"C:\Users\e11338\Desktop\Feed System GAI\data\PMI_Optimized_Core.xlsx", engine='openpyxl')
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
    print(f"計算出的導程: {guide}mm, 最接近的導程選項: {guide_f}mm")

    return guide_f
guide = Guide_calculation(maximum_feed_rate, motor_max_speed, reduction_ratio)

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
    print(f"由挫曲負荷估算導螺桿桿徑: {dr_p}mm, 由導螺桿臨界轉速估算導螺桿桿徑: {dr_n}mm, 由拉伸負荷估算導螺桿桿徑: {dr_t}mm")
    dr_F =  max(dr_n, dr_p, dr_t)
    dr_F = dr_F + 4

    #由DN估算導螺桿桿徑
    dr_DN = round(150000 / Nm, 0)
    print(f"直徑下限: {dr_F}mm, 直徑上限: {dr_DN}mm")
    print(f"{dr_F}mm < 螺桿直徑 < {dr_DN}mm")

    d_list = [8, 10, 12, 14, 15, 16, 20, 25, 28, 32, 36, 38, 40, 45, 50, 55, 60, 63, 70, 80, 100]
    suitable_dr = []
    cunt = 0
    found_any = False
    for diameter in range(len(d_list)):
        # 同時符合強度要求 (dr_F) 且在轉速限制內 (dr_DN)
        
        if d_list[diameter] >= dr_F and d_list[diameter] <= dr_DN:
            suitable_dr.append(d_list[diameter])
            cunt = diameter
            found_any = True
    if found_any and cunt+1 < len(d_list):
        suitable_dr.append(d_list[cunt+1])
    print(suitable_dr)

    return dr_F, dr_DN, suitable_dr, p, dr_t
dr_F, dr_DN, suitable_dr, p, dr_t = Diameter_calculation(gravity_axis_YN, load, cutting_force, length, maximum_feed_rate, guide, support_type)
print("="*100)
print(f"導程: {guide}")
print("="*100)

#動負荷計算
def C_calculation(cutting_force, load, gravity_axis_YN, preload_rate):
    
    if gravity_axis_YN:
            p = (load + cutting_force)
    else:
        cof = 0.008 #摩擦力係數
        ff = load * cof 
        p = (cutting_force + ff)

    c = round(p / 3 / preload_rate, 0)
    print(f"動負荷: {c} kfg")  
    return c
c = C_calculation(cutting_force, load, gravity_axis_YN, preload_rate)


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
    allowable_speed = 0.8 * (f_val * dr * (10**7)) / (length ** 2)

    # --- 反推 2：容許最大壓縮力/挫曲負荷 (kgf) ---
    # 依據尤拉公式推導，安全係數 alpha 取 0.5
    E = 21000
    alpha = 0.5
    I = (math.pi * (dr ** 4)) / 64
    allowable_buckling = alpha * (N_val * (math.pi ** 2) * E * I) / (length ** 2)

    # --- 反推 3：容許最大拉伸力 (kgf) ---
    # 依據應力公式推導
    allowable_stress = 14.7
    A = (math.pi * (dr ** 2)) / 4
    allowable_tensile = allowable_stress * A

    return allowable_speed, allowable_buckling, allowable_tensile

allowable_speed, allowable_buckling, allowable_tensile = verify_ballscrew_safety(dr_F, length, support_type="fixed_supported")
print(f"公稱外徑_mm: {dr_F}")
print(f"容許臨界轉速_rpm: {round(allowable_speed, 2)}")
print(f"容許最大壓縮力(挫曲)_kgf: {round(allowable_buckling, 2)}")
print(f"容許最大拉伸力_kgf: {round(allowable_tensile, 2)}")
print("="*100)

#計算剛性
#螺桿剛性-1 + 軸承剛性-1 + 螺帽剛性-1
#軸承內徑為型號前兩位數字，設定值為螺桿值徑-10 取最接近值 

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
    print(f"移動件所引起的摩擦扭矩: {Tt} N．mm, 軸向力引起的扭矩:{Tc} N．mm")
    print(f"外加負荷引起之扭矩: {Trf} N．mm")
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
    print(f"公稱外徑_mm: {suitable_dr[-1]}")
    print(f"負載慣量: {JL} kgf．cm．s2")
    return JL
Trf = Motor_torque_calculation(guide, load, cutting_force)
print("=" *100)
JL = Motor_inertia_calculation(length, suitable_dr, load, guide)
print()
print()
