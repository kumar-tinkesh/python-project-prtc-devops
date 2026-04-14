# Number is prime if it is greater than 1 and only has two factors 2 and itself

number = 59
count = 0
if number > 1:
    for i in range(1, number+1):
        if number % i == 0:
            count += 1

    if count == 2:
        print(f"{number} is a prime number!")
    else:
        print(f"{number} is NOT a prime number!")        
else:
    print("Enter a positive number greater than 1")