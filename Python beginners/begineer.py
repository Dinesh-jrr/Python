# #mad libs game
# color=input("Enter a color:")
# plural_noun=input("Enter a plural noun:")
# celebrity=input("Enter a celebrity:")
# print(f"Roses are {color}")
# print(f"{plural_noun} are blue")
# print("I love "+ celebrity)

###Lists
# friends=["Dinesh","Rohan","Dipesh","Akash","Subash","Kalyan","Kushal","Biswo","Manoj","Bamey"]
# # print(friends)
# # print(friends[0])
# # print(friends[-2])
# # print(friends[1:3])
# # print(friends[3:])
# friends.append("Hero")
# print(friends)

# ##Lists functions
# num=[1,2,3,4,5,6]
# friends=["Dinesh","Rohan","Dipesh","Akash","Subash","Kalyan","Kushal","Biswo","Manoj","Bamey"]
# # friends.extend(num)
# # print(friends)
# print(num.sort())

# ##Tuple
# num=(1,2,3,4,5,6)
# print(num[0])
# ##list of tuples
# num=[(4,5),(6,7)]

##Function in python
# def user(name):
#     print("Hello!", name)
# user("Dinesh")

##Return statement
# def cube(num):
#     result=num*num*num
#     # print(result)
#     return result
# cube(3)
##return break down the code from the point of its existence


##If statement
# def result():
#     # is_male=True
#     is_male=False
#     if is_male:
#         print("You are a male")
#     else:
#         print("You are not a male")
# result()

# def max_num(n1,n2,n3):
#     if n1>=n2 and n1>=n3:
#         return n1
#         # print("n1 is greatest")
#     elif n2>=n1 and n2>=n3:
#         return n2
#         # print("n2 is the greatest")
#     else:
#         return n3
#         # print("n3 is the greatest")
# print(max_num(2,3,5))
# # max_num(2,3,5)

##Building a calculator
# n1=float(input("Enter a first number:"))
# operator=input("Enter a operator:")
# n2=float(input("Enter a third number:"))
# if operator=="+":
#     print(n1+n2)
# elif operator=="-":
#     print(n1-n2)
# elif operator=="/":
#     print(n1/n2)
# elif operator=="*":
#     print(n1*n2)
# else:
#     print("Invalid operator")

##Dictionary
# month_conversion={
#     "jan": "January",
#     "feb": "February",
#     "mar": "March",
# }
# print(month_conversion["jan"])
# print(month_conversion.get("mar"))
# print(month_conversion.get("dec","Not a valid key"))


##While loop
# i=1
# while i<=10:
#     # print(i)
#     i+=1
# print(i)

##Guessing game
# secret_word="giraffe"
# guess=""
# while guess!= secret_word:
#     guess=input("Enter your guess:")
# print("You win!")

##just trying different
# secret_word="dinesh"
# guess=input("Enter your guess:")
# if guess==secret_word:
#     print("You win")
# else:
#     guesss=input(guess)

# secret_word="dinesh"
# guess=""
# guess_count=0
# guess_limit=3
# out_of_guesses=False
# while guess!=secret_word and not(out_of_guesses):
#     if guess_count<guess_limit:
#         guess=input("Enter your guess:")
#         guess_count+=1
#     else:
#         out_of_guesses=True
# if out_of_guesses:
#     print("Out of guesses,you lose!")
# else:
#     print("You win!")

    ##For loop
# for i in "Dinesh":
#     print(i)
# for i in range(1,11):
#     print(i)
# friends=["Dinesh","Neymar","Messi"]
# for i in range(len(friends)):
#     print(friends[i])

###Exponent function
# def raise_to_power(base_num,pow_num):
#     result=1
#     for i in range(pow_num):
#         result=result* base_num
#     return result
# print(raise_to_power(3,4))

##2D lists and nested loops
# number_grid=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]
# # print(number_grid[0][0])
# # print(number_grid[0][1])

# for row in number_grid:
#     for col in row:
#         print(col)
#     # print(row)


##Building a translator
# def translate():
#     phrase=input("Enter a phrase:")
#     translation=""
#     for i in phrase:
#         if i in "AEIOUaeiou":
#             translation=translation+"g"
#         else:
#             translation=translation+i
#     return translation
# print(translate())

##Try and except
# try:
#     num=int(input("Enter a number:"))
#     print(num)
# except:
#     print("Invalid number")

###read a file
# file=open("example.txt","r")
# print(file.read())
# file.close()
# with open("example.txt","r") as file:
#     print(file.read())

##writing a file

##modules and pip
#classes and objects

##multiple choice questions

# class student:
#     def __init__(self,name,major,gpa):
#         self.name=name
#         self.major=major
#         self.gpa=gpa
#         pass
#     def on_hono_roll(self):
#         if self.gpa>=3.5:
#             return True
#         else:
#             return False