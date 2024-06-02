import numpy as np 

def eulerToQuaternion(alpha, theta, gamma):
    alpha = np.radians(alpha)
    theta = np.radians(theta)
    gamma = np.radians(gamma)

    w = np.cos(alpha/2) * np.cos(theta/2) * np.cos(gamma/2) + np.sin(alpha/2) * np.sin(theta/2) * np.sin(gamma/2)
    x = np.sin(alpha/2) * np.cos(theta/2) * np.cos(gamma/2) - np.cos(alpha/2) * np.sin(theta/2) * np.sin(gamma/2)
    y = np.cos(alpha/2) * np.sin(theta/2) * np.cos(gamma/2) + np.sin(alpha/2) * np.cos(theta/2) * np.sin(gamma/2)
    z = np.cos(alpha/2) * np.cos(theta/2) * np.sin(gamma/2) - np.sin(alpha/2) * np.sin(theta/2) * np.cos(gamma/2)

    return (w, x, y, z)

def queternionToEuler(w, x, y, z):
    alpha = np.arctan2(2 * (w * x + y * z), 1 - 2 * (x ** 2 + y ** 2))
    theta = np.arcsin(2 * (w * y - x * z))
    gamma = np.arctan2(2 * (w * z + x * y), 1 - 2 * (y ** 2 + z ** 2))
    return (alpha, theta, gamma)


if __name__ == "__main__":
    quaternion = eulerToQuaternion(0, 0, 45)
    euler = queternionToEuler(0.9238795325112867, 0.0, 0.0, 0.3826834323650898)
    euler = tuple(np.degrees(degree) for degree in euler)
    print("quaternion: ", quaternion)
    print("euler: ", euler)