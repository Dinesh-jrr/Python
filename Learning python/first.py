# #Ternary operator
# def is_adult(age):
#     return True if age>=18 else False
# print(is_adult(2))

#string
# print("Dinesh".upper())
# name="dinesh"
# print(name.isupper())
# print(name.title())
# print(name.find("d"))
# print(name.isalnum())
# print("\"Din\"esh")
# done=True
# print(type(done))
# if done:
#     print("Yes")
# else:
#     print("No")

# ##Lists
# num=[1,2,3,4,5]
# num.append("Dinesh")
# num[3]="Neymar"

# print(num)
# Objects
# age=8
# print(age.real)
# print(age.imag)
# age=8
# print(age)

##Loops
# count=0
# while count<=10:
#     print("The condition is true")
#     count=count+2
# print("After the loop")

##Continue
# items=[1,2,3,4,5]
# for item in items:
#     if item==2:
#         continue
#     print(item)

# ##Break
# items=[1,2,3,4,5]
# for item in items:
#     if item==2:
#         break
#     print(item)

##Classes
# class Animal:
#     def walk(self):
#         print("Walking....")
# class dog(Animal):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def bark(self):
#         print("woof!")
# roger=dog("Roger",8)
# print(roger.name)
# print(roger.age)
# roger.bark()
# roger.walk()

##Modules
# from dog import bark
# bark()
# import math
# print(math.sqrt(4))

##Arguments from command line
##Lambda functions
# lambda num : num *2
# multiply=lambda a,b :a * b
# print(multiply(2,4))
##map(), filter(), reduce()
# numbers=[1,2,3,4]
# def isEven(n):
#     return n % 2 == 0
# result=filter(isEven,numbers)
# print(list(result))

# ## using lambda
# numbers=[1,2,3,4,5]
# result=filter(lambda n : n % 2 ==0,numbers)
# print(list(result))

##Reduce()
from functools import reduce
expenses=[
    ("Dinner",80),
    ("Car repair",120)
]
# sum=0
# for expense in expenses:
#     sum = sum + expense[1]


#alternate
sum=reduce(lambda a,b:a[1]+b[1],expenses)
print(sum)
