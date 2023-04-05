# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names = name1 + name2
names1 = names.lower().count("t") + names.lower().count("r") + names.lower().count("u") + names.lower().count("e")
names2 = names.lower().count("l") + names.lower().count("o") + names.lower().count("v") + names.lower().count("e")
score = int(str(names1) + str(names2))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")




















# Otherwise, the message will just be their score. e.g.:
# print(f"Your score is **z**.")
