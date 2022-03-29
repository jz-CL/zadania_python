"""
Write a function that takes a number n and generates â€€rst n 6-digits lucky tickets.

"""


"""

https://github.com/Darkhunter9/python/blob/master/Mathematically%20Lucky%20Tickets.py
"""


from random import randrange


def suma_3sign(v):
    sum = 0
    for i in range(len(v)):
        sum += int(v[i])
    return sum


def generate_3sign():
    # wygeneruj 3 liczby 0-9
    t = ""
    for i in range(3):
        v = randrange(10)
        t += str(v)
    return t

def generate_lucky_tickets():
    v = generate_3sign()
    su = suma_3sign(v)

    while True:
        v1 = generate_3sign()
        su1 = suma_3sign(v1)

        if su == su1:
            return v + v1

if __name__ == "__main__":
    for i in range(6):
        _ = generate_lucky_tickets()
        print(f"lucky_tickets: {i} --> {_}")