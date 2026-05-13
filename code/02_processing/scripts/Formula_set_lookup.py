### 指定輸入參數
maximum_feed_rate = 48000 #最大進給速率, mm/min
motor_max_speed = 4000 #馬達最高轉速，預設3000 rpm
acceleration = "" #加速度
reduction_ratio = 1 #減速比
load = 775 #負載
cutting_force = 343 #切削力
length = 924 # 螺桿長度，兩端軸承間距
preload_rate = 0.05 #預壓率
axis = ["x", "y", "z"]
gravity_axis_YN = True #判斷重力軸
guide = maximum_feed_rate / (motor_max_speed * reduction_ratio)
N = maximum_feed_rate / guide #螺桿最高轉速

from math import pi

# 導程 & 最大轉速，最大進給速率 = 導程 * 最大轉速 * 減速比
guide = maximum_feed_rate / (motor_max_speed * reduction_ratio) #導程

#直徑計算
def Diameter_calculation():
    Nm = (maximum_feed_rate / guide) * 0.5 #臨界轉速

    #由導螺桿臨界轉速估算導螺桿桿徑
    f = [9.7, 15.1, 21.9, 3.4] #[支-支, 固-支, 固-固, 固-自]
    dr_n = round((Nm * length**2 / f[2]) * 1e-7, 0) # dr = (n * (length**2) / f) * (10**-7)

    #由挫曲負荷估算導螺桿桿徑
    if gravity_axis_YN:
        p = (load + cutting_force) * 2
    else:
       cof = 0.008 #摩擦力係數
       ff = load * cof 
       p = (cutting_force + ff) * 2
    E = 21000 #kgf/mm2
    n = [4.0, 2.0, 0.25] #[固-支, 固-固, 固-自]
    dr_p = round((p * 64 * (length**2) / (n[0] * (pi**3) * E))**0.25, 0)
    #取大值
    print(f"由挫曲負荷估算導螺桿桿徑: {dr_p}mm, 由導螺桿臨界轉速估算導螺桿桿徑: {dr_n}mm")
    dr_F =  max(dr_n, dr_p)
    #由DN估算導螺桿桿徑
    dr_DN = round(150000 / N, 0)
    print(f"直徑下限: {dr_F}mm, 直徑上限: {dr_DN}mm")
    print(f"{dr_F}mm < 螺桿直徑 < {dr_DN}mm")

    d_list = [12, 14, 15, 16, 20, 25, 28, 32, 36, 40, 45, 50, 55, 63, 70, 80, 100]
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

    return dr_F, dr_DN, suitable_dr
dr_F, dr_DN, suitable_dr = Diameter_calculation()
print("="*100)
print(f"導程: {guide}")
print("="*100)

#動負荷計算
def C_calculation():
    
    if gravity_axis_YN:
            p = (load + cutting_force)
    else:
        cof = 0.008 #摩擦力係數
        ff = load * cof 
        p = (cutting_force + ff)

    c = round(p / 3 / preload_rate, 0)
    print(f"動負荷: {c} kfg")  
    return c
c = C_calculation()