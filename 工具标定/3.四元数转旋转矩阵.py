import numpy as np
from scipy.spatial.transform import Rotation 


def quaternionToMatrix(a, b, c, d):
    row1 = np.array([[1-2*c**2-2*d**2, 2*b*c-2*a*d, 2*a*c+2*b*d]])
    row2 = np.array([[2*b*c+2*a*d, 1-2*b**2-2*d**2, 2*c*d-2*a*b]])
    row3 = np.array([[2*b*d-2*a*c, 2*a*b+2*c*d, 1-2*b**2-2*c**2]])
    rotation_matrix = np.concatenate((row1, row2, row3), axis=0)
    return rotation_matrix

def matrixToQuaternion(rotation_matrix):
    w = np.sqrt(np.trace(rotation_matrix) + 1) / 2
    x = (rotation_matrix[2][1]- rotation_matrix[1][2]) / (4 * w)
    y = (rotation_matrix[0][2] - rotation_matrix[2][0]) / (4 * w)
    z = (rotation_matrix[1][0] - rotation_matrix[0][1]) / (4 * w)
    return (w, x, y, z)


if __name__ == "__main__":
    rotation_matrix = quaternionToMatrix(0.92387953, 0, 0, 0.38268343)
    matrix_answer = Rotation.from_quat([0, 0, 0.38268343, 0.92387953]).as_matrix()
    quaternion = matrixToQuaternion(rotation_matrix)
    print("rotation_matirx: ", rotation_matrix)
    print("matrix_answer: ", matrix_answer)
    print("quaternion: ", quaternion)
    # print(res @ np.array([1, 0, 0]))
    # print(res2@ np.array([1, 0, 0]))
    