"""绘制Ising模型的自旋构型图"""
import matplotlib.pyplot as plt
import numpy as np
import time

def plot(_data_file, flag="show", save_path=None):
    """输入文件数据，画出自旋构型图，_flag=[show|save]，保存图形或者显示图形，_save_path给出保存路径"""
    lines = []
    for line in _data_file:
        line = list(map(float, line.rstrip('\n').rstrip('\t').split('\t')))
        lines.append(line)
    data_matrix = np.array(lines)
    X, Y = np.meshgrid(np.arange(0, data_matrix.shape[1]), np.arange(0, data_matrix.shape[0]))    # 注意此处的meshgrid维度
    U = np.cos(data_matrix)
    V = np.sin(data_matrix)
    figure = plt.figure()
    # 在 https://matplotlib.org/api/pyplot_api.html 找到更多设置
    Q = plt.quiver(X, Y, U, V, units='inches', scale=12, pivot='middle')
    if flag == "save":
        save_file = 'Figure_' + str(figure.number) + '.eps'
        plt.savefig(save_path + save_file, dpi=None)
    plt.show()

def main():
    file_path = r"D:\Research\TheoryLearn\Codes\MC-XY\Data_XY.txt"
    with open(file_path, 'r', encoding='utf8') as data_file:
        plot(data_file, flag='save', save_path="D:\\")

if __name__ == '__main__':
    main()
