print('''
*******************************************************************************
        ...
             ;::::;
           ;::::; :;                    
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `# 

*******************************************************************************
''')
print("Welcome to The Pardoner's Tale Game!")
print(
    "You are three young men seeking to confront Death after your friend's demise."
)

print("\nYou are in a bustling tavern. What will you do?")
print("1. Discuss your plan openly.")
print("2. Keep your plans private.")

choice1 = input("Enter your choice: ")

if choice1 == "1":
    print(
        "\nAs you openly discuss your plan, a mysterious old man approaches.")
    print("He hints that Death can be found near a great oak tree.")
else:
    print(
        "\nYou keep your plans private and quietly leave the tavern to find Death."
    )

print("\nNow you stand before a fork in the road.")
print("1. Follow the old man's hint and head to the oak tree.")
print("2. Explore a different path.")

choice2 = input("Enter your choice: ")

if choice2 == "1":
    print("\nYou arrive at the oak tree and discover a stash of gold coins.")
    print("Now comes the moment of decision: how will you divide the gold?")
    print("1. Divide it equally among yourselves.")
    print("2. Let greed take over and grab as much gold as you can.")

    choice3 = input("Enter your choice: ")

    if choice3 == "1":
        print("\nUnited by trust, you divide the gold equally.")
        print(
            "Your camaraderie prevails, and you continue your journey together."
        )
    else:
        print(
            "\nGreed consumes you, and chaos erupts as you betray each other.")
        print("In the end, your pursuit of wealth leads to your downfall.")
else:
    print(
        "\nYou venture down a different path, avoiding the oak tree and its temptations."
    )
    print("Your decision to evade greed saves you from a tragic fate.")

print("\nRadix malorum est cupiditas - Greed is the root of all evil.")
