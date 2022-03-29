"""
Write a function which generates all evens number in range from given start to end.
Example:
generate_evens(start=1, end=12) # should return [2, 4, 6, 8, 10]

"""


def generate_evens(start, end):
    t = []
    for v in range(start, end):
        if v % 2 == 0:
            t.append(v)
    return t


if __name__ == "__main__":
    _ = generate_evens(start=1, end=12)
    print(_)
