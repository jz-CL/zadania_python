"""

write a function that takes two numeric values and returns their maximum.
You're allowed to use only if-else statements.

Example:
    my_max(10, 20) # Should return 20

"""


def my_max(v1, v2):
    if v1 > v2:
        return v1
    else:
        return v2


if __name__ == "__main__":
    v = my_max(10, 20)
    print(v)
