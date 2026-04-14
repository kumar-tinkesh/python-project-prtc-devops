# Factorial of a number

number = 5
factorial = 1

if number < 0:
    print("Please enter a number greater than 0")
elif number == 0:
    print(f"Factorial of {number} is 1. ")
else:
    for i in range(1, number+1):
        factorial = factorial * i

    print(f"Factorial of {number} is {factorial}!")


# recursive function 
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
    
# one liner
    # return 1 if (n==1 or n==0) else n * factorial(n-1)

print(f"Factorial of {number} is {factorial(5)}!")