import numpy as np
import scipy.linalg as linalg
import math
#参数分别是旋转轴和旋转弧度值
b = np.array([[1, 0, 0],
             [0, np.cos(np.pi), -np.sin(np.pi)],
             [0, np.sin(np.pi), np.cos(np.pi)]])
a = np.array([[np.cos(np.pi * 3/ 2), -np.sin(np.pi*3 /2), 0],
          [np.sin(np.pi *3/2), np.cos(np.pi * 3/ 2), 0],
          [0, 0, 1]])

c = np.dot(b, a)