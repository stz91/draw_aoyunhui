    # coding=utf-8
    import matplotlib.pyplot as plt
    import numpy as np

    # 这两行代码解决 plt 中文显示的问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 输入产量与温度数据
    production = [1125, 1725, 2250, 2875, 2900, 3750, 4125]
    tem = [6, 8, 10, 13, 14, 16, 21]
    rain = [25, 40, 58, 68, 110, 98, 120]

    colors = np.random.rand(len(tem))  # 颜色数组
    size = production
    plt.scatter(tem, rain, s=size, c=colors, alpha=0.6)  # 画散点图, alpha=0.6 表示不透明度为 0.6
    plt.ylim([0, 150])  # 纵坐标轴范围
    plt.xlim([0, 30])   # 横坐标轴范围
    plt.xlabel('温度')  # 横坐标轴标题
    plt.ylabel('降雨量')  # 纵坐标轴标题
    plt.show()