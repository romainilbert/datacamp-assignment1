# noqa: D100
import numpy as np


def max_index(X):
    """Return the index of the maximum in a numpy array.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        The input array.

    Returns
    -------
    i : int
        The row index of the maximum.

    j : int
        The column index of the maximum.

    Raises
    ------
    ValueError
        If the input is not a numpy error or
        if the shape is not 2D.
    """
    i = 0
    j = 0

    # TODO
    if type(X) is not np.ndarray:
        raise ValueError('The input is not a np array')
    if len(X.shape) !=2 :
        raise ValueError('X is not a matrix')
    (i,j)=np.unravel_index(np.argmax(X,axis=None), X.shape)
    return i, j


def wallis_product(n_terms):
    """Implement the Wallis product to compute an approximation of pi.

    See:
    https://en.wikipedia.org/wiki/Wallis_product

    XXX : write Parameters and Returns sections as above.

    """
    pi = 0.0

    for i in range(n_term):
        left = (2 * i)/(2 * i - 1)
        right = (2 * i)/(2 * i + 1)
        total = left * right
        pi = pi + total

    return pi
    # XXX : The n_terms is an int that corresponds to the number of
    # terms in the product. For example 10000
