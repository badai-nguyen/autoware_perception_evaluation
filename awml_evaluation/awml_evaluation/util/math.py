import math

import numpy as np


def rotation_matrix_to_euler(rotation_matrix: np.ndarray) -> np.ndarray:
    """[summary]
    Convert rotation matrix to euler angles.

    Args:
        rotation_matrix (np.ndarray): The 3x3 array of rotation matrix.

    Returns:
        np.ndarray: The 3D array, [roll, pitch, yaw].
    """
    assert _is_rotation_matrix(rotation_matrix)

    sy: float = math.sqrt(rotation_matrix[0, 0] ** 2 + rotation_matrix[1, 0] ** 2)
    singular: bool = sy < 1e-6

    if not singular:
        roll: float = math.atan2(rotation_matrix[2, 1], rotation_matrix[2, 2])
        pitch: float = math.atan2(-rotation_matrix[2, 0], sy)
        yaw: float = math.atan2(rotation_matrix[1, 0], rotation_matrix[0, 0])
    else:
        roll: float = math.atan2(-rotation_matrix[1, 2], rotation_matrix[1, 1])
        pitch: float = math.atan2(-rotation_matrix[2, 0], sy)
        yaw: float = 0.0

    return np.array([roll, pitch, yaw])


def _is_rotation_matrix(rotation_matrix: np.ndarray) -> bool:
    """[summary]
    Check whether input matrix is rotation matrix.

    Args:
        rotation_matrix (np.ndarray): 3x3 array.

    Returns:
        bool: Whether input matrix is rotation matrix.
    """
    rot_mat_t = np.transpose(rotation_matrix)
    should_be_identity: np.ndarray = np.dot(rot_mat_t, rotation_matrix)
    identity: np.ndarray = np.identity(3, dtype=rotation_matrix.dtype)
    norm: float = np.linalg.norm(identity - should_be_identity)
    return norm < 1e-6
