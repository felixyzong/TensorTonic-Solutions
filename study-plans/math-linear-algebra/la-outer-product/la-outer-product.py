import numpy as np

def outer_product(u, v):
    """
    Returns: float64 matrix of shape (m, n), the outer product u v^T.
    """
    ret = np.zeros((len(u),len(v)))
    for i in range(len(u)):
        for j in range(len(v)):
            ret[i,j] = u[i] * v[j]
    return ret