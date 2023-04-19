# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

num_items = len(names)
rand_choice = random.randint(0, num_items -1)
payer = names[rand_choice]
print(f"{payer} is going to buy the meal today!")




#Shorter and better  👇
#randomname = random.choice(names)
#print(f"{randomname} is going to buy the meal today!")