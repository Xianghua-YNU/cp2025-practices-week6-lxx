import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# 系统参数
m = 1.0  # 质量(kg)
k = 1.0  # 弹簧系数(N/m)
total_time = 10.0  # 总模拟时间(s)
initial_position = 0.0  # 修改初始位置为0.0以匹配测试用例
initial_velocity = 0.0  # 初始速度(m/s)

def solve_ode_euler(step_num):
    """
    使用欧拉法求解弹簧 - 质点系统的常微分方程。
    """
    # 创建存储位置和速度的数组
    position = np.zeros(step_num + 1)
    velocity = np.zeros(step_num + 1)
    
    # 计算时间步长
    time_step = total_time / step_num
    
    # 设置初始位置和速度
    position[0] = initial_position
    velocity[0] = initial_velocity
    
    # 使用欧拉法迭代求解微分方程
    for i in range(1, step_num + 1):
        acceleration = -k * position[i-1] / m
        velocity[i] = velocity[i-1] + acceleration * time_step
        position[i] = position[i-1] + velocity[i-1] * time_step
    
    # 生成时间数组
    time_points = np.linspace(0, total_time, step_num + 1)
    
    return time_points, position, velocity

def spring_mass_ode_func(state, time):
    """
    定义弹簧 - 质点系统的常微分方程。
    """
    x, v = state  # 解包位置和速度
    dxdt = v  # 位置的导数是速度
    dvdt = -k * x / m  # 速度的导数是加速度
    return [dxdt, dvdt]

def solve_ode_odeint(step_num):
    """
    使用 odeint 求解弹簧 - 质点系统的常微分方程。
    """
    # 设置初始条件
    initial_state = [initial_position, initial_velocity]
    
    # 创建时间点数组
    time_points = np.linspace(0, total_time, step_num + 1)
    
    # 使用 odeint 求解微分方程
    solution = odeint(spring_mass_ode_func, initial_state, time_points)
    
    # 从解中提取位置和速度
    position = solution[:, 0]
    velocity = solution[:, 1]
    
    return time_points, position, velocity

def plot_ode_solutions(time_euler, position_euler, velocity_euler, 
                       time_odeint, position_odeint, velocity_odeint):
    """
    绘制欧拉法和 odeint 求解的位置和速度随时间变化的图像。
    """
    plt.figure(figsize=(12, 6))
    
    # 绘制位置对比图
    plt.subplot(1, 2, 1)
    plt.plot(time_euler, position_euler, 'b-', label='Euler Position')
    plt.plot(time_odeint, position_odeint, 'r--', label='odeint Position')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.title('Position vs Time')
    plt.legend()
    plt.grid(True)
    
    # 绘制速度对比图
    plt.subplot(1, 2, 2)
    plt.plot(time_euler, velocity_euler, 'b-', label='Euler Velocity')
    plt.plot(time_odeint, velocity_odeint, 'r--', label='odeint Velocity')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Velocity vs Time')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # 模拟步数
    step_count = 1000
    
    # 使用欧拉法求解
    time_euler, position_euler, velocity_euler = solve_ode_euler(step_count)
    
    # 使用 odeint 求解
    time_odeint, position_odeint, velocity_odeint = solve_ode_odeint(step_count)
    
    # 绘制对比结果
    plot_ode_solutions(time_euler, position_euler, velocity_euler, 
                       time_odeint, position_odeint, velocity_odeint)
