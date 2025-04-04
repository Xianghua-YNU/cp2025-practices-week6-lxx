import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy import constants

def plot_wien_equation():
    """绘制维恩方程的两个函数图像"""
    # 创建x轴数据点
    x = np.linspace(0, 10, 500)
    
    # 创建图形
    plt.figure(figsize=(10, 6))
    
    # 绘制两条曲线
    plt.plot(x, 5*np.exp(-x), 'b-', label='y = 5e$^{-x}$')
    plt.plot(x, 5 - x, 'r--', label='y = 5 - x')
    
    # 设置坐标轴和标题
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.title('Graphical Solution of Wien\'s Equation', fontsize=14)
    
    # 添加图例和网格
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # 显示图形
    plt.show()

def wien_equation(x):
    """维恩方程：5e^(-x) + x - 5 = 0"""
    return 5*np.exp(-x) + x - 5

def solve_wien_constant(x0=5.0):
    """求解维恩位移常数"""
    # 使用fsolve求解非线性方程
    x = fsolve(wien_equation, x0)[0]
    
    # 计算维恩位移常数
    h = constants.h
    c = constants.c
    k = constants.k
    b = h*c / (k*x)
    
    return x, b

def calculate_temperature(wavelength, x0=5.0):
    """根据波长计算温度"""
    # 获取维恩位移常数
    _, b = solve_wien_constant(x0)
    
    # 计算温度
    return b / wavelength

if __name__ == "__main__":
    # 绘制方程图像
    print("绘制维恩方程图像...")
    plot_wien_equation()
    
    # 从键盘输入初值
    try:
        x0 = float(input("请根据图像输入方程求解的初始值（建议值为4-6）："))
    except ValueError:
        print("输入无效，将使用默认值 5")
        x0 = 5
    
    # 计算维恩位移常数
    x, b = solve_wien_constant(x0)
    print(f"\n使用初值 x0 = {x0}")
    print(f"方程的解 x = {x:.6f}")
    print(f"维恩位移常数 b = {b:.6e} m·K")
    print(f"文献值 b ≈ 2.8977729e-3 m·K")
    
    # 计算太阳表面温度
    wavelength_sun = 502e-9  # 502 nm 转换为米
    temperature_sun = calculate_temperature(wavelength_sun, x0)
    print(f"\n太阳表面温度估计值：{temperature_sun:.0f} K")
    print("实际观测值约为5778 K")
