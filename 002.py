"""

Write a function that takes three numeric parameters and returns their maximum.
You're allowed to use only if-else statements.

Example:
my_max3(10, 20, 100) # should return 100

"""


def my_max(v1, v2):
    if v1 > v2:
        return v1
    return v2


def my_max3(v1, v2, v3):
    _ = my_max(v1, v2)
    return my_max(_, v3)


if __name__ == "__main__":
    _ = my_max3(10, 20, 100)
    print(_)
