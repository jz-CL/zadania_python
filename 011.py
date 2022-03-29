"""
We call a natural number x > 1 a prime number if and only if it has only 2 divisors, e.g 1 and x
itself. Write a function is prime which takes a natural number x and returns true if x is prime
and false otherwise.

Example:
is_prime(10) # should False
is_prime(7) # should True

"""

"""
https://pl.wikipedia.org/wiki/Sito_Eratostenesa

"""


def is_prime(n):
    if n < 2:
        return "n < 2"

    t = []
    for i in range(1, n + 1):
        t.append((i, True))


"""
    jak sprawdzić czy określona liczba jest liczbą pierwszą

    dana liczba 5
    czy 5 jest podzielne przez 2, 3, 4 ?



"""

return n

if __name__ == "__main__":
    _ = is_prime(5)
    print(f"jest liczbą pierwszą")

