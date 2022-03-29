"""
Write a function filter_nums which returns list of values which are not divisible by 3.

Example:
filter_nums([1, 8, 7, 10, 9, 6, 3]) # should return [1, 8, 7, 10]
"""


def filter_nums(vl):
    t = []
    for v in vl:
        if v % 3 != 0:
            t.append(v)
    return t


if __name__ == "__main__":
    _ = filter_nums([1, 8, 7, 10, 9, 6, 3])
    print(_)
