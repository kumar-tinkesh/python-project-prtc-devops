# Decorators are functions
# Decorators wrap other functions and enhance their behaviour
# Decorators are examples of higher order function
# Decorators have their own syntax


def be_polite(func):
    def wrapper():
        print("what a pleasure to meet you")
        func()
        print("Good Luck\n")
    return wrapper


@be_polite
def greet():
    print("My name is Sidd.")


@be_polite
def rage():
    print("Who are you.")


greet()
rage()
