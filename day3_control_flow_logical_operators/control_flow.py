print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("You ride for free!!!!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    photo = input("Do you want photos taken? Y or NO: ")
    if photo == "Y":
        bill += 3

    print(f"Your final price is ${bill}")
else:
    print("You cannot ride the rollercoaster!")
