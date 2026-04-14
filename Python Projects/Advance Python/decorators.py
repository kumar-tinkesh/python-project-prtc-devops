from random import choice
# higher order functions


def sum(n, func):
    total = 0
    for num in range(1, n+1):
        total += func(num)
    return total


def square(x):
    return x * x


def cube(x):
    return x * x * x


print(sum(5, square))
print(sum(5, cube))
print("******************")


def greet(person):
    def get_mood():
        msg = choice(("Hello there ", "Go Away ", "I love you "))
        return msg

    result = get_mood() + person
    return result


print(greet("Toby"))

# function returing a function


def make_laugh():
    def get_laugh():
        msg = choice(("Hahahaha ", "lolz", "hehehehe"))
        return msg

    return get_laugh


laugh = make_laugh()
print(laugh())

# closure. function returing a function with parameters


def make_laugh_at(person):
    def get_laugh():
        msg = choice(("Hahahaha ", "lolz", "hehehehe"))
        return f"{msg} {person}"

    return get_laugh


laugh_at = make_laugh_at("Jerry")
print(laugh_at())
