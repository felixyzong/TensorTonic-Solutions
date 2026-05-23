import numpy as np

def linear_combination(vectors, coefficients):
    """
    Returns: float64 array, the weighted sum of vectors.
    """
    comb = np.zeros(len(vectors[0]))
    for i in range(len(vectors)):
        comb += np.array(vectors[i]) * coefficients[i]

    return comb