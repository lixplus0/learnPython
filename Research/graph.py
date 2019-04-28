"""绘制Ising模型的自旋构型图"""
import matplotlib.pyplot as plt
import numpy as np


def plot(_data_file):
    """输入文件数据，画出自旋构型图"""
    lines = []
    for line in _data_file:
        line = list(map(float, line.rstrip('\n').rstrip('\t').split('\t')))
        lines.append(line)
    S = np.array(lines)
    X, Y = np.meshgrid(np.arange(0, S.shape[0]), np.arange(0, S.shape[0]))
    U = np.cos(S)
    V = np.sin(S)
    plt.figure()
    Q = plt.quiver(X, Y, U, V, units='inches')
    plt.show()

def main():
    file_path = r"D:\Research\TheoryLearn\Codes\MC-XY\Data_XY.txt"
    with open(file_path, 'r', encoding='utf8') as data_file:
        plot(data_file)



if __name__ == '__main__':
    main()