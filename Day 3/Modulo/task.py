# Modulo Operator
# Gives an output which is remainder of the division

# 10 / 3 Has 1 as remainder so 10 modulo 3 should be 1
# print(10 % 3)

print("Welcome to the 'Is the number odd or even?' machine!")
given_number = int(input("Please write the number you want to check:\n"))
result = (given_number % 2)
if result == 1:
    print("The number you have chosen is odd!")
else:
    print("The number you have chosen is even!")
