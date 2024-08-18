fruits = ["Cherry", "Apple", "Pear"]

print(fruits[0])

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
                     "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
                     "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee",
                     "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
                     "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada",
                     "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington",
                     "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska",
                     "Hawaii"]
# print(len(states_of_america))
# print(states_of_america[0])
# Negative Indices
# print(states_of_america[-50])

states_of_america[1] = "Pencilvania"
states_of_america.append("Dogusland")
states_of_america.extend(["Koksalsas", "Lokmania"])

print(states_of_america)