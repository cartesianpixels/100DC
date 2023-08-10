# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? (Pick a number between 1 and 3 please) : ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇


if int(position[0]) > 3 or int(position[0]) < 1 or int(position[1]) > 3 or int(position[1]) < 1:
	print("You are out of range, type a position between 1 and 3")
else:
	column = int(position[0]) - 1 
	row = int(position[1]) - 1
	map[row][column] = 'X'
	print(f"{row1}\n{row2}\n{row3}")


#Write your code above this row 👆

# 🚨 Don't change the code below 👇

