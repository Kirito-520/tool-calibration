import numpy as np

def unitVectorRotation(theta, unit_vec, vec):
    theta = np.radians(theta)
    temp1 = np.cos(theta)*vec 
    temp2 = (1 - np.cos(theta)) * unit_vec@vec * unit_vec
    temp3 = np.sin(theta) * np.cross(unit_vec, vec)
    res = temp1 + temp2 + temp3

    return res 

if __name__ == "__main__":
    unit_vec = np.array([0, 0, 1])
    vec = np.array([1, 0, 0])
    matrix = unitVectorRotation(45, unit_vec, vec)
    print("the matrix of the rotation is :\n", matrix)



