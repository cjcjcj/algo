"""
    Reservoir sampling allows to randomly
    choose k samples from a list of n items,
    where n is either a very large or unknown number
"""

import random

def reservoir_sampling(sample: list[float], k):
    r = sample[:k]
    n = len(sample)

    for i in range(k, n):
        j = random.uniform(0, i)
        if j < k:
            r[j] = sample[i]
    return r
