"""
In some unknown country, all bus tickets have 6-digits serial numbers (example: 000123, 321982).
We say that a ticket is lucky if the sum of the â€€rst 3 numbers is equal to the sum of the last 3
numbers. Write a function is lucky which takes a string with 6-digits ticket serial number and
returns true if a ticket is lucky and false otherwise.

"""


def suma_3sign(v):
    sum = 0
    for i in range(len(v)):
        sum += int(v[i])
    return sum


def is_lucky(v):
    v1 = suma_3sign(v[0:3])
    v2 = suma_3sign(v[3:6])

    return v1 == v2


if __name__ == "__main__":
    _ = is_lucky("321982")
    print(f"jest {_}")