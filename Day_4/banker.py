# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
list_len = len(names)
#Write your code below this line 👇
index = random.randint(0,list_len-1)
banker = names[index]
print(f"{banker} is going to buy the meal today!")