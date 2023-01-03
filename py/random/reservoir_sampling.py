"""
    Reservoir sampling allows to randomly
    choose k samples from a list of n items,
    where n is either a very large or unknown number
"""

import random


def reservoir_sampling(sample: list[float], k):
    """
        https://ru.wikipedia.org/wiki/Reservoir_sampling#%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_R
    """
    r = sample[:k]
    n = len(sample)

    for i in range(k, n):
        j = random.uniform(0, i)
        if j < k:
            r[j] = sample[i]
    return r
