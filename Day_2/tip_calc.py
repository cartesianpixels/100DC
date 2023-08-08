#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
meal = float(input("What's the cost of your meal? "))
tip = float(input("What's the tip you would like to give? 10 12 15? "))
individual = float(input("What's the number of people splitting the bill? "))
tipped = (tip / 100) + 1
cost = ( meal / individual ) * tipped
print("Each person should pay $%.2f" % cost)