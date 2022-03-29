"""
You are given a list of integers. Write a function that nds maximum and minimum value in
that list and returns a tuple. You are allowed to use only if-else and loop statements.
Example:
minmax([10, 1, 22, 19, 30]) # should return (1, 30)

"""


def minmax(vl):
    v_min = 0
    v_max = 0

    counter = 0
    for v in vl:
        if counter < 1:
            v_min = v
            v_max = v

        #  max
        if v_max < v:
            v_max = v

        # min
        if v_min > v:
            v_min = v

        counter += 1
    return v_min, v_max


if __name__ == "__main__":
    _ = minmax([10, 1, 22, 19, 30])
    print(_)
