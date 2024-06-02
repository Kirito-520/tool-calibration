import numpy as np
complex_num = np.array([[1, -1], [1, 1]])
matrix1 = np.array([[1], [0]])
res = complex_num@matrix1
print(res.shape)
print(res)

