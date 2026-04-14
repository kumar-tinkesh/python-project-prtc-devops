from datetime import datetime

str_value = "python 😄"
num_value = 999
print(f"the str value is {num_value}")
# OUTPUT :  the str value is python
print(f"{num_value=}")
# OUTPUT : num_value=999
print(f'{num_value = }')  # spaces
# OUTPUT : num_value = 999
print(f"{num_value * 2 = }")
# OUTPUT : num_value * 2 = 1998
print(f"{str_value!a}") # ascii characters
# OUTPUT : 'python  \U0001f604'

num_value = 99.1234
now = datetime.utcnow()
print(f"{now}")
# OUTPUT : 2022-04-28 09:51:59.881359
print(f"{now=:%y-%m-%d}")
# OUTPUT : now=22-04-28
print(f"{now=:%Y}")  #OUTPUT : now=04/28/22
print(f"{num_value:.2f}")
# OUTPUT : 99.12
rounded_to_two = ".2f"
print(f"{num_value:{rounded_to_two}}")
# OUTPUT : 99.12
