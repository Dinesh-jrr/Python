################Rock,Paper and scissors game
# import random
# def get_choices():
#     player_choice=input("Enter a choice(rock,paper.scissors:)")
#     options=["rock","paper","scissors"]
#     computer_choice=random.choice(options)
#     choices={"player":player_choice, "computer":computer_choice}
#     return choices

# def check_win(player,computer):
#     print(f"You chose {player} , computer chose {computer}")
#     if player==computer:
#         return "It's a tie!"
#     elif player=="rock": 
#         if computer=="scissors":
#             return "Rock smashes scissors!you win"
#         else:
#             return"Paper covers rock!You lose."
#     elif player=="paper":
#         if computer=="rock":
#             return "Paper covers rock!you win"
#         else:
#             return "Scissors cuts paper!you lose"
#     elif player=="scissors":
#         if computer=="paper":
#             return "Scissors cuts paper!you win"
#         else:
#             return "Rock smashes scissors!You lose."
# choices=get_choices()
# result=check_win(choices["player"],choices["computer"])
# print(result) 

####Practice
# name="Dinesh"
# age=20
# print(name)
# print(age)
# print(type(age))
# print(float(age))
# print(len(name))
# print("DInesh" + "Jr")
# list=[1,2,3,4]
# if 1 in list:
#     print("It is there")
# age=20
# print(str(age))
   


# print("Dinesh".upper() + "Jr".lower()) #To translate the string into upper and lower cases 
# print("DInesh".islower())##To check if all the letter are in lowercase
####
#title()- to get a capitalized version of a string
#startswith()- to check if the string starts with a specific substring
#endswith() to check if the string ends with a specific substring
#replace()- to replace a part of a string
#split()- to split a string in a specific character separator
#strip()- to trim the whitespace form a string
#join()- to append new letters to a string
##find()- to find the position of a stirng
# name="Dinesh"
# print(name.find("D"))
# print(name.upper())
# print("esh" in name)

# print("Din\"esh\"")##To add "" in between the string 
# age=10
# print(isinstance(age,int))
# name="Dinesh:"
# print(name[2:5])

####any,all 

##built in function
# print(abs(-5.5))
# print(round(5.40,1))
###USe of append,remove,insert
# items=["Dinesh","Messi","Neymar"]
# items.sort
# print(items)

####lists,tuple,dictinary,set
set1={1,2,3,4}
set2={1,2,3,4,5,6}
check=set1 & set2
print(check)

