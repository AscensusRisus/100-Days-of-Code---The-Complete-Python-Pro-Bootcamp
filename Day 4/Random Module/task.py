import random as random

# import my_module
#
# random_integer = random.randint(1, 3)
# print(random_integer)
# print(my_module.my_favourite_number)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)

coinflip_input = input("Welcome to the coin flip game! Choose your side heads or tails?\n").lower()
random_number = random.random() * 10
if random_number < 5:
    result = "tails"
else:
    result = "heads"
if result == coinflip_input:
    match_result = "won!"
else:
    match_result = "lost"
print(f"It is {result}. You {match_result}")
