# """
# To print numbers from 1  to 10
# """
# for i in range(1,11):
#     print(i)
 
# """
#  TO print all the odd numbers between 1 and 15
#  """
# for i in range(1,16,2):
#     print(i)

# """
#  TO calculate the sum of first 10 natural numbers
#  """
# sum=0
# for i in range(1,11):
#     sum=sum + i 
##### Lists example
# num=[1,2,3,4,5,6,7,8,9]
# print("Before append:",num)
# num.append(11)
# print("After append:",num)
# num.insert(3,"A")
# print( "After insert:",num)
# num.extend(["A","B","C"])
# print("After extend:",num)

# num=[1,2,3,4]
# num_copy=num
# num.append("Z")
# print(num_copy)
# num.append(7,8,9)
# print(num_copy)
# a=10
# b=a
# a=11
# b=a
# print(b)
# num=[1,2,3,4,5,6,7,8,9]
# del num[3]
# print("After removal:",num)
# num.remove(6)
# print("After removal:",num) 
# num=[1,2,3,4,5,6,7,8]
# for character in (num):
# #     print(character)
# num=[3.1,3.2,3.3]
# print(num)
# number=[1,2,3,num,4,5,6,7]
# print(number)
# number.append("A")
# print(number)
# print(number[3][3])
# L=["a",["bb",["ccc","ddd"],"ee","ff"],"g","h"]
# print(L[1])
# print(L[1][1])
# print(L[1][1][0])
# print(L[1][2])
# print(L[1][1][-1])

# num=[1,2,3,4,5,6,7,8,9]
# sum=0
# for i in num:
#     sum=sum+i

# print(sum)

#Tuple example
# a=(10)
# print(type(a))
#Ro print the square of the number in the list in list format
# num=[2,4,6]
# num_sqr=[]
# for i in num:
#     num_sqr.append(i**2)


# print(num_sqr)

# num=[1,2,3]
# num_sqr=[i**2 for i in num]
# print(num_sqr)
    
# num=[4,5,6]
# num_cube=[i**3 for i in num]
# print(num_cube)
 
# numbers=[1,2,3,4,5]
# squares=[x**2 for x in numbers]
# print(squares)
 
# num=[1,2,3,4,5]
# even_numbers=[x for ]
# """
# Multiplication table
# """
# def multiplication_table():
#     #This is a doc string 
#     num= int(input("Enter a number:"))
#     for i in range(1, num +1):
#         for j in range(1,num+1):
#             result= i*j
#             print(result, end=" ")
#         print()
# multiplication_table()

