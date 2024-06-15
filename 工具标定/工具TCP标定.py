import numpy as np
from scipy.spatial.transform import Rotation as R


def euler2rotation(alpha, theta, gamma, euler_mode):
    rotation_matrix = R.from_euler(euler_mode, [alpha, theta, gamma], degrees=True).as_matrix()
    return rotation_matrix

def rotation_differences(rotation_list):
    rotation_diff_list = []
    for i in range(len(rotation_list)-1):
        rotation_diff_list.append(rotation_list[i] - rotation_list[i+1])
    return rotation_diff_list

def position_differences(position_list):
    position_diff_list = []
    for i in range(1, len(position_list)):
        position_diff_list.append(position_list[i] - position_list[i-1])
    return position_diff_list

def sample_to_position_rotation(sample_list, euler_mode):
    position_list = []
    rotation_list = []
    for i in range(len(sample_list)):
        rotation_list.append(euler2rotation(*sample_list[i][3:], euler_mode))
        position_list.append(np.array(sample_list[i][:3]).reshape(3, 1))

    return (position_list, rotation_list)
    

def tcp_calibration(position_list, rotation_list):   
    position_diff_list = position_differences(position_list)
    rotation_diff_list = rotation_differences(rotation_list)

    p_matrix = np.concatenate(position_diff_list, axis=0)
    R_matrix = np.concatenate(rotation_diff_list, axis=0)
                        
    R_transpose = R_matrix.T
   
    res = np.linalg.inv(R_transpose @ R_matrix) @ R_transpose @ p_matrix 

    return res 

def orientation_calibration(orientation_matrix, euler_mode):
    r_matrix = euler2rotation(*orientation_matrix[3:], euler_mode)
    r_matrix = np.linalg.pinv(r_matrix)
    rotation = R.from_matrix(r_matrix)
    euler_angles = rotation.as_euler('ZYX', degrees=True)
    return euler_angles


if __name__ == "__main__":
    sample_list = [[539.93,-7.63,466.87,16.93,-24.34,176.41],
                   [658.30, -85.61, 500.47, 108.21, -4.04, 162.42],
                   [742.53, -5.41, 525.69, -175.42, 9.00, 175.73],
                   [683.28, 46.64, 521.81, -84.13, 4.39, -170.77]]
    orientation_matrix = [636.75,53.04,735.19,-173.37,41.51,-179.56]
    
    (position_matrix, rotation_matrix) = sample_to_position_rotation(sample_list, "ZYX")
 
    position_vector = tcp_calibration(position_matrix, rotation_matrix).reshape(3,)

    euler_angles = orientation_calibration(orientation_matrix, "ZYX")

    T_matrix = position_vector.tolist() + euler_angles.tolist()

    print(T_matrix)
