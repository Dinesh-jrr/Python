
# """
# To find whether a given number is
# positive or negative
# """
# def number():
#     num1=int(input("Enter a number:"))
#     if num1>0:
#         print("The number is postive")
#     else:
#         print("The number is negative")

# number()

# """
# To find whether the given year is leap
# year or not
# """
# def result():
#     year=int(input("Enter a year:"))
#     if (year % 400 ==0) and (year % 100 ==0):
#         print(f"{year} is leap year") 
#     if (year % 4 ==0) and (year % 100 !=0):
#         print( f"{year} is not a leap year")

# result()
# """
# To check whether a person is eligilble
# for voting or not
# """
# def result():
#     Age=int(input("Enter a age:"))
#     if Age>=18:
#         print("Eligilbe")
#     else:
#         print("Not eligible")

# result()
# """
# To find the lowest number out of two numbers
# expected from users
# """
# def result():
#     num1=int(input("Enter a number:"))
#     num2=int(input("Enter a second number:"))
#     if num1>num2:
#         print("num2 is lowest")
#     else:
#         print("num1 is lowest")

# result()
# """
# To find whether a number is divisible by 
# 2 and 3 both
# """
# def result():
#     num1=int(input("Enter a number:"))
#     if num1%2==0 and num1%3==0:
#         print("divisible")
#     else:
#         print("Not divisible")

# result()

# """
# To check whether a character is a vowel 
# or consonant
# """
# def result():
#     character=str(input("Enter a character:"))
#     if character=="a" or character=="e" or character=="i" or character=="o" or character=="u":
#         print("Vowel")
#     else:
#         print("Consonant")

# result()
# """
# To accept any city from the user and 
# display tourist attractions of that city
# """
# def display():
#     city=str(input("Enter a city:"))
#     if city=="kathmandu":
#        print("Pashupatinath Temple")
#     elif city=="Pokhara":
#         print("Fewa Lake")
#     elif city== "Nepalgunj":
#         print("Bageswari Temple")
#     else:
#         print("Birgunj Ghanta Ghar")

# display()
# """
# TO calculate the percentage of class attended
# when total number of working days and absent days 
# are given

# """
# def calculate():
#     n1=int(input("Enter total number of working days:"))
#     n2=int(input("Enter total number of absent days:"))
#     percentage=(((n1-n2)/n1)*100)
#     print(percentage)
#     if percentage<80:
#         print("Students willnot stay in the exam" )
#     else:
#         print("Students will stay in the exam")

# calculate()
# """
# To find if the student will be able to sit the exam 
# ot not after calculating percentage
# """
# def calculate():
#     num1=int(input("Enter a mark obtained by student:"))
#     num2=int(input("Enter total marks of the subject:"))
#     percentage=((num1/num2)*100)
#     if percentage>=80:
#         print("Will be able to sit in exam")
#     else:
#         print("Will not be able to sit in exam")

# calculate()

# """
#  TO take three numbers as input and display the largest
#  of the three numbers using if-else statements
#  """
# def display():
#      num1=int(input("Enter a first number:"))    
#      num2=int(input("Enter a second number:"))
#      num3=int(input("Enter a third number:"))
#      if num1>num2 and num1>num3:
#         print("num1 is largest")
#      elif num2>num1 and num2>num3:
#         print("num2 is largest")
#      else:
#         print("num3 is largest")
# display()

# """
# To find the BMI of user and display a message of the 
# user is normal weight, overweight or obese
# """
# def calculate():
#     num1=int(input("Enter a height of user in centimeters:"))
#     num2=int(input("Enter a weight of user in kilograms:"))
#     BMI=(num1/(num2**2))
#     print(BMI)
#     if 18.5<= BMI<25:
#         print("Normal weight")
#     elif 25<=BMI<30:
#         print("Overweight")
#     else:
#         print("Obese")
# calculate()

# """ 
#    To calculate the difference between a given number
#    and 17 and if the number is greater than 17 return
#    twice the absolute difference
# """
# def display():
#     num1=int(input("Enter a number:"))
#     num2=17
#     difference=(num1-num2)
#     if difference>17:
#         print(difference*2)
#     else:
#         print(difference)

# display()
 


# """
# # Addition
# # """
# def calculate():
#     num1=int(input("Enter a number:"))
#     num2=int(input("Enter a number:"))
#     output=format(num1+num2,".2f")
#     return output

# calculate()
# """
# Subtraction
# """
# def calculator():
#     num1=int(input("Enter a number:"))
#     num2=int(input("Enter a number:"))
#     result=format(num1-num2,".2f")
#     return result

# calculator()
# """
# Multiplication
# """
# def calculator():
#     num1=int(input("Enter a number:"))
#     num2=int(input("Enter a number:"))
#     result=format (num1*num2,".2f")
#     return result

# calculator()
# """
# Division
# """
# def calculator():
#     num1=int(input("Enter a number:"))
#     num2=int(input("Enter a number:"))
#     result=format (num1/num2,".2f")
#     return result

# calculator()
# """
# Modulus
# """
# def caculator():
#     num1=int(input("Enter a number:"))
#     num2=int(input("Enter a number:"))
#     result=format(num1%num2,".2f")
#     return result

# calculator()
# """
# Exponentiation
# num1 and num2 are parameters
# result is the square of num1 to num2
# """
# def calculator():
#     num1=int(input("Enter a number:"))
#     num2=int(input("Enter a number:"))
#     result=format(num1**num2,".2f")
#     return result

# calculator()
# print(calculator.__doc__)

# """
# To convert given time into hours,minute and seconds
# """
# def convert():
#     total_time=13442
#     print("total time to wait for train:",total_time)
#     hours=total_time//3600
#     remaining=total_time%3600
#     min=remaining//60
#     remaining=remaining%60
#     sec=remaining
#     print("total time to wait for train:",hours,"hours", min,
#           "minutes",sec,"seconds")

# convert()

# """
# To find the average of marks of five students,
# total marks and the peercentage
# """
# def result():
#     num1=int(input("Enter a first score:"))
#     num2=int(input("Enter a second score:"))
#     num3=int(input("Enter a third score:"))
#     num4=int(input("Enter a fourth score:"))
#     num5=int(input("Enter a fifth score:"))
#     Average=(num1+num2+num3+num4+num5)/5
#     print(Average)
#     sum=num1+num2+num3+num4+num5
#     print(sum)
#     percentage=format(Average*100,".2f")
#     print(percentage)

# result()
