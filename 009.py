"""
Write a function which takes list of numbers and returns list of numbers powered to n (which is
given) modulo m (which is also given).

Example:
compute(nums=[1, 2, 3], n=10, m=7) # should return [1 ** 10 % 7, 2 ** 20 % 7, 3 ** 10 % 7]

"""


def compute(nums, n, m):
    t = []
    for v in nums:
        t.append(v ** n % m)
    return t


if __name__ == "__main__":
    _ = compute(nums=[1, 2, 3], n=10, m=7)
    print(_)
