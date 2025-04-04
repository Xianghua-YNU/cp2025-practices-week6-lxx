import numpy as np
import matplotlib.pyplot as plt

def simulate_beat_frequency(f1=440, f2=444, A1=1.0, A2=1.0, t_start=0, t_end=1, num_points=5000, show_plot=True):
    """
    拍频现象的数值模拟
    参数说明:
        f1, f2: 两个波的频率(Hz)
        A1, A2: 两个波的振幅
        t_start, t_end: 时间范围(s)
        num_points: 采样点数
        show_plot: 是否显示图像
    返回:
        t: 时间数组
        superposed_wave: 叠加波形
        beat_frequency: 拍频频率
    """
    # 生成时间范围
    t = np.linspace(t_start, t_end, num_points)
    
    # 生成两个正弦波
    wave1 = A1 * np.sin(2 * np.pi * f1 * t)
    wave2 = A2 * np.sin(2 * np.pi * f2 * t)

    # 叠加两个波
    superposed_wave = wave1 + wave2

    # 计算拍频
    beat_frequency = abs(f1 - f2)

    # 绘制图像
    if show_plot:
        plt.figure(figsize=(12, 8))
        
        # 绘制第一个波
        plt.subplot(3, 1, 1)
        plt.plot(t, wave1, 'b', label=f'频率{f1}Hz, 振幅{A1}')
        plt.title('第一个正弦波')
        plt.xlabel('时间 (s)')
        plt.ylabel('振幅')
        plt.legend()
        plt.grid(True)
        
        # 绘制第二个波
        plt.subplot(3, 1, 2)
        plt.plot(t, wave2, 'g', label=f'频率{f2}Hz, 振幅{A2}')
        plt.title('第二个正弦波')
        plt.xlabel('时间 (s)')
        plt.ylabel('振幅')
        plt.legend()
        plt.grid(True)
        
        # 绘制叠加波
        plt.subplot(3, 1, 3)
        plt.plot(t, superposed_wave, 'r', label=f'合成波 (拍频:{beat_frequency}Hz)')
        plt.title('叠加波形 - 拍频现象')
        plt.xlabel('时间 (s)')
        plt.ylabel('振幅')
        plt.legend()
        plt.grid(True)

        plt.tight_layout()
        plt.show()

    return t, superposed_wave, beat_frequency

def parameter_sensitivity_analysis():
    """
    参数敏感性分析
    1. 分析不同频率差对拍频的影响
    2. 分析不同振幅比例对拍频的影响
    """
    # 频率差分析
    plt.figure(1, figsize=(12, 8))
    base_freq = 440  # 基准频率
    delta_fs = [1, 2, 5, 10]  # 频率差列表
    t = np.linspace(0, 1, 5000)
    
    for i, delta_f in enumerate(delta_fs):
        f2 = base_freq + delta_f
        wave1 = np.sin(2 * np.pi * base_freq * t)
        wave2 = np.sin(2 * np.pi * f2 * t)
        superposed_wave = wave1 + wave2
        
        plt.subplot(len(delta_fs), 1, i+1)
        plt.plot(t, superposed_wave, label=f'频率差:{delta_f}Hz, 拍频:{delta_f}Hz')
        plt.xlabel('时间 (s)')
        plt.ylabel('振幅')
        plt.legend()
        plt.grid(True)
    
    plt.suptitle('不同频率差对拍频现象的影响')
    plt.tight_layout()
    
    # 振幅比例分析
    plt.figure(2, figsize=(12, 8))
    f1, f2 = 440, 442  # 固定频率
    amp_ratios = [(1,1), (1,0.5), (1,0.2), (0.5,1)]  # 振幅比例列表
    
    for i, (A1, A2) in enumerate(amp_ratios):
        wave1 = A1 * np.sin(2 * np.pi * f1 * t)
        wave2 = A2 * np.sin(2 * np.pi * f2 * t)
        superposed_wave = wave1 + wave2
        
        plt.subplot(len(amp_ratios), 1, i+1)
        plt.plot(t, superposed_wave, label=f'A1/A2={A1}/{A2}')
        plt.xlabel('时间 (s)')
        plt.ylabel('振幅')
        plt.legend()
        plt.grid(True)
    
    plt.suptitle('不同振幅比例对拍频现象的影响')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # 示例调用
    print("=== 任务1: 基本拍频模拟 ===")
    t, wave, beat_freq = simulate_beat_frequency(f1=440, f2=444, t_end=0.5)
    print(f"计算得到的拍频为: {beat_freq} Hz")
    
    print("\n=== 任务2: 参数敏感性分析 ===")
    parameter_sensitivity_analysis()
