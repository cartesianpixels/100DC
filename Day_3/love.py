# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()

substring_t = "t"
count_t1 = lowercase_name1.count(substring_t)
count_t2 = lowercase_name2.count(substring_t)
count_t = count_t1 + count_t2
#print(f"T occurs {count_t} times")

substring_r = "r"
count_r1 = lowercase_name1.count(substring_r)
count_r2 = lowercase_name2.count(substring_r)
count_r = count_r1 + count_r2
#print(f"R occurs {count_r} times")

substring_u = "u"
count_u1 = lowercase_name1.count(substring_u)
count_u2 = lowercase_name2.count(substring_u)
count_u = count_u1 + count_u2
#print(f"U occurs {count_u} times")

substring_e = "e"
count_e1 = lowercase_name1.count(substring_e)
count_e2 = lowercase_name2.count(substring_e)
count_e = count_e1 + count_e2
#print(f"E occurs {count_e} times")

total1 = count_t + count_r + count_u + count_e
#print(f"Total is {total1}")

substring_l = "l"
count_l1 = lowercase_name1.count(substring_l)
count_l2 = lowercase_name2.count(substring_l)
count_l = count_l1 + count_l2
#print(f"L occurs {count_l} times")

substring_o = "o"
count_o1 = lowercase_name1.count(substring_o)
count_o2 = lowercase_name2.count(substring_o)
count_o = count_o1 + count_o2
#print(f"O occurs {count_o} times")

substring_v = "v"
count_v1 = lowercase_name1.count(substring_v)
count_v2 = lowercase_name2.count(substring_v)
count_v = count_v1 + count_v2
#print(f"V occurs {count_v} times")
total2 = count_l + count_o + count_v + count_e
#print(f"Total is {total2}")
love_total = int(f"{total1}{total2}")
#print(f"Love score is {love_total}")

if love_total < 10  or love_total > 90:
  print(f"Your score is {love_total}, you go together like coke and mentos.")
elif love_total < 50  and love_total > 40:
  print(f"Your score is {love_total}, you are alright together.")
else:
  print(f"Your score is {love_total}.")