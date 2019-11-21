import random


def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    return factorial


if __name__ == "__main__":
    while True:
        n = random.choice(range(1, 5))
        f = factorial(n=n)

        print("Factorial of {n} is {f}".format(n=n, f=f))
