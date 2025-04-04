import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def sineWaveZeroPhi(x, t, A, omega, k):
    '''
    返回位置x和时间t的波函数值
    参数:
    x : 空间位置 (array)
    t : 时间 (float)
    A : 振幅 (float)
    omega : 角频率 (float)
    k : 波数 (float)
    '''
    return A * np.sin(k * x - omega * t)

# 创建动画所需的 Figure 和 Axes
fig = plt.figure(figsize=(10, 6))
subplot = plt.axes(xlim=(0, 10), xlabel="Position (m)", 
                  ylim=(-2.2, 2.2), ylabel="Displacement (m)")
plt.title('Standing Wave Formation', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)

# 创建空的line对象，用于动画显示
line1, = subplot.plot([], [], 'b-', lw=2, label='Right-moving wave')
line2, = subplot.plot([], [], 'g-', lw=2, label='Left-moving wave')
line3, = subplot.plot([], [], 'r-', lw=3, label='Standing wave')

# 导出lines变量以满足测试要求
lines = [line1, line2, line3]

# 创建空间变量x并导出
x = np.linspace(0, 10, 1000)

def init():
    '''动画初始化函数'''
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return lines

def animate(i):
    '''动画更新函数'''
    # 定义波的参数
    A = 1
    omega = 2 * np.pi * 0.5  # 降低频率使动画更清晰
    k = np.pi / 2
    t = 0.05 * i  # 减慢时间变化
    
    # 计算两个方向相反的波
    y1 = sineWaveZeroPhi(x, t, A, omega, k)
    y2 = sineWaveZeroPhi(x, t, A, -omega, k)  # 方向相反
    
    # 计算驻波（两波之和）
    y3 = y1 + y2
    
    # 更新波形数据
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    line3.set_data(x, y3)
    
    return lines

if __name__ == '__main__':
    # 创建动画对象
    anim = FuncAnimation(fig, animate, init_func=init,
                        frames=200, interval=50, blit=True)
    
    # 显示动画
    plt.show()
    
    # 如需保存动画，取消下面注释
    # anim.save('standing_wave.mp4', writer='ffmpeg', fps=30)
