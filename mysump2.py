def mysum2(numbers, start = 0):
    total = start
    for number in numbers:
        total += number
    return total

# print(mysum2([1,2,3,4],30))


assert mysum2([1,2,3]) == 6
assert mysum2([1,2,3], 4) == 10
assert mysum2([]) == 0
assert mysum2([], 5) == 5
assert mysum2([-1, -2]) == -3
assert mysum2([1.5, 2.5], 1) == 5.0
assert mysum2([10**6, 10**6], 10**6) == 3_000_000

try:
    mysum2(["a", "b"])
    raise AssertionError("Expected TypeError for non-numeric elements")
except TypeError:
    pass


def mysum(numbers, start=0):
    """
    Sum numbers with an optional starting value.

    >>> mysum([1, 2, 3])
    6
    >>> mysum([1, 2, 3], 4)
    10
    >>> mysum([])
    0
    >>> mysum([], 5)
    5
    """
    total = start
    for num in numbers:
        total += num
    return total

if __name__ == "__main__":
    import doctest
    doctest.testmod()


# Think in examples. A tiny checklist catches most bugs:

# happy path: ([1, 2, 3], start=0) → 6

# with start: ([1, 2, 3], start=4) → 10

# empty input: ([], start=0) → 0, ([], start=5) → 5

# negatives: ([-1, -2], start=0) → -3

# floats: ([1.5, 2.5], start=1) → 5.0

# big numbers: ([10**6, 10**6], start=10**6) → 3_000_000

# type safety (should error): (["a", "b"]) → TypeError