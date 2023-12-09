import math

alphabet = ' abcdefghijklmnopqrstuvwxyz'


def enbase(x):
    n = len(alphabet)
    if x < n:
        return alphabet[int(x)]
    return enbase(x / n) + alphabet[int(x) % n]


def debase(x):
    n = len(alphabet)
    result = 0
    for i, c in enumerate(reversed(x)):
        result += alphabet.index(c) * (n ** i)
    return result


def pad(x, n):
    p = alphabet[0] * (n - len(x))
    return '%s%s' % (x, p)


def str_average(a, b):
    n = max(len(a), len(b))
    a = debase(pad(a, n))
    b = debase(pad(b, n))
    return enbase((a + b) / 2)

def str_diff(a, b):
    n = max(len(a), len(b))
    a = debase(pad(a, n))
    b = debase(pad(b, n))

    return math.sqrt(a - b)
