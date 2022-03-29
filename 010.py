"""
Write a function that finds the roots of a quadratic equation. The general form of quadratic
equation is ax2 + bx + c = 0, where a != 0. Develop a function solve equation which takes
coeffcients a, b and c in as input and solves the equation. You are free to use any pythonic
mechanism you are familiar with to solve the problem.

"""
"""
https://realpython.com/python-import/

https://www.matemaks.pl/proste-rownania-kwadratowe.html
https://pl.wikipedia.org/wiki/R%C3%B3wnanie_kwadratowe

"""

from math import sqrt


def qe_delta(a, b, c):
    return b * b - 4 * a * c


def quadratic_equation(a, b, c):
    # test a
    if a == 0:
        return "a jest równe 0"

    delta = qe_delta(a, b, c)

    if delta < 0:
        return "brak rozwiązań, delta < 0"

    if delta > 0:

        x1 = (-b - sqrt(delta)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)

        return f"x1 = {x1}, x2 = {x2}"

    else:
        x1 = -b / (2 * a)
        return f"x = {x1}"


if __name__ == "__main__":
    _ = quadratic_equation(2, 8, -10)

    print(_)
