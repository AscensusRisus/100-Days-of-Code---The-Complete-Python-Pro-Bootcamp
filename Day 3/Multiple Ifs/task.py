print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    total_bill = 0
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child tickets are $5")
        total_bill += 5
    elif age <= 18:
        print("Youth tickets are $7")
        total_bill += 7
    else:
        print("Adult tickets are $12")
        total_bill += 12

    photo = input("For only $3 would you like to your photo taken while on ride? ")
    if photo == "yes":
        total_bill += 3
    # elif photo == "no":
        # total_bill += 0
    print(f"your total bill is ${total_bill}.")
else:
    print("Sorry you have to grow taller before you can ride.")


