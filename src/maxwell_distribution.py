import numpy as np
from scipy.integrate import quad
import time
import matplotlib.pyplot as plt

# 最概然速率 (m/s)
vp = 1578  

def maxwell_distribution(v, vp):
    """
    计算麦克斯韦速率分布函数值
    """
    coeff = 4 / np.sqrt(np.pi) * (v**2 / vp**3)
    exponent = - (v**2 / vp**2)
    return coeff * np.exp(exponent)

def percentage_0_to_vp(vp):
    """
    计算速率在0到vp间隔内的分子数百分比
    """
    result, _ = quad(maxwell_distribution, 0, vp, args=(vp,))
    return result * 100

def percentage_0_to_3_3vp(vp):
    """
    计算速率在0到3.3vp间隔内的分子数百分比
    """
    result, _ = quad(maxwell_distribution, 0, 3.3*vp, args=(vp,))
    return result * 100

def percentage_3e4_to_3e8(vp):
    """
    计算速率在3×10^4到3×10^8 m/s间隔内的分子数百分比
    """
    result, _ = quad(maxwell_distribution, 3e4, 3e8, args=(vp,))
    return result * 100

def trapezoidal_rule(f, a, b, n, vp):
    """
    使用梯形法则计算麦克斯韦分布的积分
    """
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x, vp)
    return h * (0.5*y[0] + 0.5*y[-1] + np.sum(y[1:-1])) * 100

def percentage_0_to_vp_trap(vp, n):
    return trapezoidal_rule(maxwell_distribution, 0, vp, n, vp)

def percentage_0_to_3_3vp_trap(vp, n):
    return trapezoidal_rule(maxwell_distribution, 0, 3.3*vp, n, vp)

def percentage_3e4_to_3e8_trap(vp, n):
    return trapezoidal_rule(maxwell_distribution, 3e4, 3e8, n, vp)

def compare_methods(task_name, quad_func, trap_func, vp, n_values=[10, 100, 1000, 10000]):
    """比较quad和梯形积分法的结果和性能"""
    print(f"\n{task_name}的方法对比:")
    
    # 使用quad计算（作为参考值）
    start_time = time.time()
    quad_result = quad_func(vp)
    quad_time = time.time() - start_time
    print(f"quad方法: {quad_result:.6f}%, 耗时: {quad_time:.6f}秒")
    
    # 使用不同区间划分数的梯形法则
    print("\n梯形积分法结果:")
    print(f"{'区间划分数':<12}{'结果 (%)':<15}{'相对误差 (%)':<15}{'计算时间 (秒)':<15}")
    
    for n in n_values:
        start_time = time.time()
        trap_result = trap_func(vp, n)
        trap_time = time.time() - start_time
        rel_error = abs(trap_result - quad_result) / quad_result * 100
        
        print(f"{n:<12}{trap_result:<15.6f}{rel_error:<15.6f}{trap_time:<15.6f}")

def plot_distribution(vp):
    """绘制麦克斯韦速率分布曲线"""
    v = np.linspace(0, 5*vp, 1000)
    fv = maxwell_distribution(v, vp)
    
    plt.figure(figsize=(10, 6))
    plt.plot(v, fv, 'b-', linewidth=2)
    plt.xlabel('速率 (m/s)', fontsize=12)
    plt.ylabel('分布函数 f(v)', fontsize=12)
    plt.title('麦克斯韦速率分布 (vp=1578 m/s)', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # 标记重要区域
    plt.axvline(x=vp, color='r', linestyle='--', label=f'最概然速率 vp={vp} m/s')
    plt.axvline(x=3.3*vp, color='g', linestyle='--', label=f'3.3vp={3.3*vp:.1f} m/s')
    plt.legend(fontsize=10)
    
    plt.show()

if __name__ == "__main__":
    # 绘制分布曲线
    plot_distribution(vp)
    
    # 测试代码
    print("=== 使用quad方法的结果 ===")
    print(f"0 到 vp 间概率百分比: {percentage_0_to_vp(vp):.6f}%")
    print(f"0 到 3.3vp 间概率百分比: {percentage_0_to_3_3vp(vp):.6f}%")
    print(f"3×10^4 到 3×10^8 间概率百分比: {percentage_3e4_to_3e8(vp):.6f}%")
    
    print("\n=== quad方法与梯形积分法对比 ===")
    compare_methods("任务1: 0到vp", percentage_0_to_vp, percentage_0_to_vp_trap, vp)
    compare_methods("任务2: 0到3.3vp", percentage_0_to_3_3vp, percentage_0_to_3_3vp_trap, vp)
    compare_methods("任务3: 3e4到3e8", percentage_3e4_to_3e8, percentage_3e4_to_3e8_trap, vp)
