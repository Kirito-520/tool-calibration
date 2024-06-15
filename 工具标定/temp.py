import numpy as np
from scipy.spatial.transform import Rotation as R

def euler2rotation(alpha, theta, gamma):
    """
    alpha: 绕x轴的角度
    theta: 绕y轴的角度
    gamma: 绕z轴的角度
    """
    rotation = R.from_euler('ZYX', [alpha, theta, gamma], degrees=True)
    return rotation.as_matrix()

def rotation_differences(rotations):
    diffs = []
    for i in range(len(rotations) - 1):
        diff = rotations[i] - rotations[i + 1]
        diffs.append(diff)
    return np.array(diffs)

def position_differences(positions):
    diffs = []
    for i in range(1, len(positions)):
        diff = positions[i] - positions[i - 1]
        diffs.append(diff)
    return np.array(diffs)

def tcp_calibration(rotations, positions):
    # 计算旋转矩阵差分
    rotation_diffs = rotation_differences(rotations)

    # 计算位置差分
    position_diffs = position_differences(positions)

    # 构建旋转差分矩阵和位置差分矩阵
    R_matrix = np.concatenate(rotation_diffs, axis=0)
    p_matrix = np.concatenate(position_diffs, axis=0)

    # 转置旋转差分矩阵
    R_transpose = R_matrix.T

    # 求解方程 R.T * R * b = R.T * p
    b = np.linalg.inv(R_transpose @ R_matrix) @ R_transpose @ p_matrix

    return b

# 示例数据
rotations = [
    euler2rotation(16.93,-24.34,176.41),
    euler2rotation(108.21, -4.04, 162.42),
    euler2rotation(-175.42, 9.00, 175.73),
    euler2rotation(-84.13, 4.39, -170.77)
]

positions = [
    np.array([539.93,-7.63,466.87]).reshape(3, 1),
    np.array([658.30, -85.61, 500.47]).reshape(3, 1),
    np.array([742.53, -5.41, 525.69]).reshape(3, 1),
    np.array([683.28, 46.64, 521.81]).reshape(3, 1)
]

# 运行TCP标定算法
tool_center_point = tcp_calibration(rotations, positions)

print("Tool Center Point (TCP) Position:\n", tool_center_point)
