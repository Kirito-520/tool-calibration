import numpy as np 


def matrixToQuaternion(rotation_matrix):
    w = np.sqrt(np.trace(rotation_matrix) + 1) / 2
    x = (rotation_matrix[2][1]- rotation_matrix[1][2]) / (4 * w)
    y = (rotation_matrix[0][2] - rotation_matrix[2][0]) / (4 * w)
    z = (rotation_matrix[1][0] - rotation_matrix[0][1]) / (4 * w)
    return (w, x, y, z)



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


if __name__ == "__main__":
    rotation_matrix = euler2rotation(0, 0, 45)
    quaternion = matrixToQuaternion(rotation_matrix)
    print("rotation_matrix:", rotation_matrix)
    print("queternion: ", quaternion)
    # print(rotation_matrix @ np.array([1, 0, 0 ]))