"""

Write a function that calculates the n-th number of Fibonacci's series. Recall n-th Fibonacci's
can be determined by the following formula Fn = Fn-1 + Fn-2, F0 = 0, F1 = 1.
Example:
fib(0) # should return 0
fib(1) # should return 1
fib(2) # should return 1

"""


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    _ = fib(19)
    print(_)
