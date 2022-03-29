"""
Write your implementation of abs built-in function. Recall, abs is an absolute value of a number.
We say that the result of abs(x) is x when x is positive (or equal to 0) and -x when x is negative.
Example:

my_abs(10) # should return 10
my_abs(-10) # should return 10


"""


def my_abs(v):
    if v < 0:
        return -v
    return v


if __name__ == "__main__":
    _ = my_abs(-10)
    print(_)
