import numpy as np

def euclidean_distance(x, y):
    """
    Returns: float, the Euclidean distance between x and y.
    """
    x_np = np.array(x)
    y_np = np.array(y)

    sum = np.sum((x_np - y_np) ** 2)

    return np.sqrt(sum)