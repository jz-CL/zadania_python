"""

Write a function that takes a list of integers and returns a list in which minimum and maximum
values are swapped.
Example:
sweap([5, 9, 1, 2, 3, 4, 0]) # should return [5, 0, 1, 2, 3, 4, 9]

"""

def sweap(vl):
    v_min = 0
    v_max = 0
    index_min = -1
    index_max = -1

    counter = 0


    for v in vl:
        if counter < 1:
            v_min = v
            index_min = counter
            v_max = v
            index_max = counter

        #  max
        if v_max < v:
            v_max = v
            index_max = counter

        # min
        if v_min > v:
            v_min = v
            index_min = counter

        counter += 1

    v = vl[index_min]
    vl[index_min] = vl[index_max]
    vl[index_max] = v

    return vl



if __name__ == "__main__":
    _ = sweap([5, 9, 1, 2, 3, 4, 0])
    print(_)
