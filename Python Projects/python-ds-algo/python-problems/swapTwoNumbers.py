num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("******** With Temp variable ********")
print(f"Two Numbers: {num1} & {num2}")

temp = num1
num1 = num2 
num2 = temp 

print(f"Swapped Two Numbers: {num1} & {num2}")


print("\n******** Without Temp variable ********")
num1, num2 = num2, num1
print(f"Swapped Two Numbers: {num1} & {num2}")