# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


import art
print(art.logo)
maximum_bid = 0
equality_check = 0
bidders = {}
winner_of_the_bid = ""
bidContinues = True
other_bidders_check = "yes"
while bidContinues:
    if other_bidders_check == "yes":
        bidder_name = input("What is your name?: ")
        bid = int(input("What's your bid?: $"))
        bidders[bidder_name] = bid
        other_bidders_check = "asd"
    else:
        other_bidders_check = input("Are they any other bidders? Type 'yes' or 'no'.  \n")
        if other_bidders_check == "no":
            bidContinues= False
        if other_bidders_check == "yes":
            print("\n" * 25)

print("\n" * 25)

for key in bidders:
    maximum_bid = max(maximum_bid, bidders[key])

for key in bidders:
    if maximum_bid == bidders[key]:
        winner_of_the_bid = key

print(f"The winner is {winner_of_the_bid} with ${maximum_bid}.")

