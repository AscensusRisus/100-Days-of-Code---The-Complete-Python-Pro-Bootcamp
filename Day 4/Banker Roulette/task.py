import random
friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]

random_number = random.randint(1, 5)
if random_number == 1:
    roulette = "Alice"
elif random_number == 2:
    roulette = "Bob"
elif random_number == 3:
    roulette = "Charlie"
elif random_number == 4:
    roulette = "David"
else:
    roulette = "Emmanuel"
print(f"{roulette} has to pay!")

# print(random.choice(friends))
# random_index = random.randint(0, 4)
# print(friends[random_index])
