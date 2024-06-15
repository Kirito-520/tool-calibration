import numpy as np

def euler2rotation(alpha, theta, gamma):
    """
    alpha: 绕x轴的角度
    theta: 绕y轴的角度
    gamma: 绕z轴的角度
    """
    gamma = np.radians(gamma)
    theta = np.radians(theta)
    alpha = np.radians(alpha)
    Rz = np.array([[np.cos(gamma), -np.sin(gamma), 0],
                   [np.sin(gamma), np.cos(gamma), 0],
                   [0, 0, 1]])
    
    Ry = np.array([[np.cos(theta), 0, np.sin(theta)],
                   [0, 1, 0],
                   [-np.sin(theta), 0, np.cos(theta)]])
    
    Rx = np.array([[1, 0, 0],
                   [0, np.cos(alpha), -np.sin(alpha)],
                   [0, np.sin(alpha), np.cos(alpha)]])
    
    return Rz@Ry@Rx 

sample_rotation1 = euler2rotation(16.93, -24.34, 176.41)
sample_rotation2 = euler2rotation(108.21, -4.04, 162.42)
sample_rotation3 = euler2rotation(-175.42, 9, 175.73)
sample_rotation4 = euler2rotation(-84.13, 4.39, -170.77)
sample_list = [sample_rotation1, sample_rotation2, sample_rotation3, sample_rotation4]
h_tmp = []
for i in range(len(sample_list)-1):
    h_tmp.append(sample_list[i] - sample_list[i+1])

h_matrix = np.concatenate([h for h in h_tmp], axis=0)
h_trans_matrix = h_matrix.T
h_matrix1 = np.linalg.inv(h_trans_matrix@h_matrix) @ h_trans_matrix


pos_matrix1 = np.array([539.93, -7.63, 466.87]).reshape(3,1)
pos_matrix2 = np.array([658.30, -85.61, 500.47]).reshape(3,1)
pos_matrix3 = np.array([742.53, -5.41, 525.69]).reshape(3,1)
pos_matrix4 = np.array([683.28, 46.64, 521.81]).reshape(3,1)
pos_list = [pos_matrix1, pos_matrix2, pos_matrix3, pos_matrix4]
pos_temp = []
for i in range(1, len(pos_list)):
    pos_temp.append(pos_list[i] - pos_list[i-1])
pos_matrix = np.concatenate([p for p in pos_temp], axis=0)


res = h_matrix1@pos_matrix
print(res)