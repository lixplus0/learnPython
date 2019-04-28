import matplotlib.pyplot as plt
import numpy as np
import copy
import os


def plot(S):
    X, Y = np.meshgrid(np.arange(0, S.shape[0]), np.arange(0, S.shape[0]))
    U = np.cos(S)
    V = np.sin(S)
    plt.figure()
    Q = plt.quiver(X, Y, U, V, units='inches')
    plt.show()


filePath = "D:\Research\TheoryLearn\Codes\MC-XY\Data_XY.txt"
f = open(filePath, 'r', encoding='utf8')
lines = f.readlines()
for i in range(0, len(lines)):
    lines[i] = list(map(float, lines[i].rstrip('\n').rstrip('\t').split('\t')))
    # print(lines[i].rstrip('\n').rstrip('\t').split('\t'))
NS = np.array(lines)
plot(NS)
