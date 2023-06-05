
# # printing 1 to 10
# i=1
# while i<11: # i=+11
#     print(i)
#     i=i+1
# number=int(input("Enter a number:"))
# while number!=0:
#     print("You finally pressed zero,Thank you")

# num=int(input("Enter a number:"))
# sum=0
# while num!=0:
#     sum=sum+num
    
# print("sum")
#example of break
i=1
# while i<=10:
#     print("6*",(i),"=",6*i)
#     if i>=5:
#         break
#     i=i+1
# sum=0
# while True:
#     num=int(input("Enter a positive integer(or enter 0 to stop):"))
#     if num==0:
#         break
#     elif num<0:
#         print("Invalid input. Please enter a positive integer.")
#         continue
#     elif num%2==0:
#         print("Skipping even number.")
#         continue
#     else:
#         sum+=num
#         print(f" The current sum is {sum}.")
        
# Print(f"The final sum is {sum}.")
#validating the input
# valid_input=False
# #  For loop##range
# for i in range(0,10,2):
#     print(i)
# a= range(0,10)
# for i in a:
#     print(i)

# #sequence
# for i in "Hello":
#     print(i)

# List1=[1,2,3,4,5,"Hello"]
# for i in List1:
#     print(i)
# #Multiplication table[Use of nested for loop]
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end="\t")
#     print()
#prompt the user to enter any number
# num=float(input("Enter a number:"))
# def either_side(num):
#     less=num-1
#     more=num+1
#     return less,more
# print(either_side(num))
# 
# """
# To print the numbers from 1 to 10
# """  
# #Take variable "i"
# i=1
# for i in range(0,11):
#     print(i)
#     i=i+1
# """
# TO print sum of 10 numbers
# """
# def result(num,sum):

#     while num<=10:
#      sum=sum+num
#      num=num+1
#     print(sum)

# result(0,0)


# """
# To print all the odd numbers between 1 and 15
# """
# i=1
# for i in range(3,15,2):
#     print(i)
#     i=i+2


# """
# TO print the multiplication table of that number
# """
# #prompt the user to input a positive integer
# num=int(input("Enter a positive integer:"))
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)

# """
# To find the factorial value of any number entered through keyboard.
# """
# # Take any number from user
# num=int(input("Enter a number:"))
# for i in range(1,6):
#     print(num*i)
# """
# To take the input from user till the user wants and 
# at the end it should display the count of positive,negative and zeros entered
# """
# #take the input from the user


#print sum of number from 1 to 10
# num=0
# sum=0
# for num in range(1,11):
#     sum=sum+num
    

# print(sum)
# """
# Accept the marked price from the user and calculate 
# the net price
# """
# num=int(input("Enter a marked price:"))#take the marked price from user
# discount=10
# def result():
#     net_amount=(num-discount)
#     print(net_amount)

# result()
# """
# To sum two given integers and if the sum is between 
# 15 and 20 return 20
# """
# def result(num1,num2):
#     sum=num1+num2
#     if sum>=15 and sum<=20:
#         return 20
#     return sum
    
# if __name__ == "__main__":
#     print(result(9,10)) 
# 
# """
# Takes the two numbers from user and if both the numbers
# are positive return the product of the numbers 
# else return 0
# """
# def product(x,y):
#     if x>0 and y >0 :
#         return x * y
#     return 0

# if __name__ == "__main__":
#     print(product(1,-2))

# """
# Takes two numbers and print out whether their sum is even 
# or odd
# """
# def result(n1,n2):#take two numbers n1 and n2
#     sum=n1+n2 # add two numbers
#     if sum % 2 == 0:
#        print(f" The sum of {n1} and {n2} is even.")
#     else:
#        print(f"The sum of {n1} and {n2} is odd.")

# if __name__ == "__main__":
#    print(result(6,8))

# """
# To check if the num is between 0 and 100 and display
# within range
# """
# def check(num):
#     if num >= 0 and num <= 100 :
#         print("Within range")
#     else:
#         print("Out of range")
# if __name__ == "__main__":
#     check(111)

# """
# Rewriting the if-else statement using a single if 
# statement and else statement
# """
# def check(temperature):
#     if temperature >= 85 and humidity > 60:
#         print("Muggy day today")
#     elif temperature >= 65:
#         print("Warm, but not muggy today")
#     elif temperature <=45:
#         print("Cold today")
#     else:
#         print("Cool today")

# check(34)

# """
# To display the word with respect to the input of the user
# """
# fruit=str(input("Enter a letter:"))#take the input from user
# if fruit == "A":
#     print("Apple")
# else:
#      if fruit== "B":
#         print("Banana")
#      else :
#          if fruit== "C":
#              print("Coconut")
#          else:
#             print("None")

# """"
# To take the number from student and display as per the 
# number entered
# """
# credit= float(input("Enter a number of college credits:"))
# if credit >= 90:
#     print("Senior Status") 
# elif credit>= 60:
#     print("Junior Status")
# elif credit >= 30:
#     print("Sophomore Status")
# else:
#     print("Freshman Status")

# """
# To take a number from the user and display as per the 
# number entered
# """
# num=int(input("Enter a number:"))
# if num % 3 ==0 and num % 5 == 0:# if num is divisible by both
#     print("FizzBuzz")

# elif num % 5 == 0: #if num is divisible by 5
#     print("Buzz")
# elif num % 3 == 0:# if num is divisible by 3
#     print("Fizz")
# else:
#     print("None")

# """
# Sum of first 10 natural numbers
# """
# def sum_of_natural_numbers():
#     #function for sum of natural numbers
#     sum=0
#     for i in range(1,11):
#         sum=sum+i
#     print(f"The sum of first 10 natural numbers is {sum}")
# sum_of_natural_numbers()

# """"
# Take the positive number from user and display its 
# multiplication
# """
# def multiplication():
#     #take the function multiplication
#     num=int(input("Enter a positive number:"))
#     if num<0:
#         print("Not a positive number")
#     else:
#         for i in range(1,11):
#             print(f"{num} * {i}= {num* i}")
# multiplication()

# """
# To display the facorial value of any number taken from the user
# """
# def display():
#     num=int(input("Enter a number:"))
#     multiply=1
#     for i in range(1,num+1):
#         multiply*=i
#     print(f"The factorial value of {num} is {multiply}")
# display()

### question no 7
# def check():
#     """
#     Take the function and input from the user until the user enter
#     q or Q
#     """
#     positive=0
#     negative=0
#     zeroes=0
#     while 1:
#         num=(input("Enter a number:"))
#         if num=="q" or num=="Q":
#             break
#         num=float(num)
#         if num>1:
#             positive+=1
#         elif num<1:
#             negative+=1
#         else:
#             zeroes+=1
#     print(f"You have entered positive numbers {positive} times")
#     print(f"You have entered negative numbers {negative} times")
#     print(f"You have entered zero {zeroes} times ")
# check()


# """
# TO print fibonacci series of the nth term
# where the nth term is taken from user
# """
# def fibonacci_number_upto(num):
#     #build the function
#     fibonaccies=[0,1]
#     #create the list where initial for fibonacci series are always 0,1
#     for i in range(num-2):
#         #get the last two digit in list using slicing
#         last_two_digit=fibonaccies[-2:]
#         new_value=sum(last_two_digit)
#         fibonaccies.append(new_value)

#     print(f"Fibonacci series upto {num} terms are:")
#     for number in fibonaccies:
#         print(number)
# nth_term=int(input("Enter nth term to print fibonacci series upto:"))
        
# fibonacci_number_upto(nth_term)
# """
# Program to reverse a string
# """
# def reverse_string(string):
#     #take a string
#     reversed_string=""
#     #Iterate backward with a step off -1(for reverse)
#     for i in range(len(string)-1,-1,-1):
#         #starts from the last index so the first character would be string[-1]
#         #which is h and so on
#         character =string[i]
#         reversed_string+=character
#     return reversed_string
# print(reverse_string("DineshJr"))
# """
# To display first 7 multiples of 7
# """
# def first_multiple_of_7():
#     #create a function
#     for i in range(1,8):
#         print(f"7 * {i} = {7*i}")
# first_multiple_of_7()
# """
# TO print multiplication of first 20 numbers
# divisible by 5
# """
# def multiplication():
#     #create a function
#     for i in range(1,21):
#         print(f"5 * {i} = {5*i}")
# multiplication()
# """
# To print multiplication table of 2,4 and 5 using loop
# """
# def multiplication():
#     numbers=[2,4,5]
#     for number in numbers:
#         #Iterate over 2,4 and 5
#         for i in range(1,11):
#             #print multiplication of 2,4 and 5
#             print(f"{number} * {i} = {number*i}")
#         print("-----------------------")
# multiplication()
# """
# TO calculate the sum of all numbers between 1 and 100
# that are divisible by both 3 and 5 using loop
# """
# def result():
#     #define a function
#     sum=0
#     for i in range(1,101):
#         #take a range between 1 and 101
#         if i % 3 == 0 and i % 5 == 0:
#             sum+=i
#     print(f"Sum of all numbers between 1 and 100 that are divisible by both 3 and 5 is {sum}")
# result()
# """
# TO calculate the sum of all numbers between 1 and 100
# that are  not divisible by both 3 and 5 using loop
# """
# def result():
#     #define a function
#     sum=0
#     for i in range(1,101):
#         #take a range between 1 and 101
#         if i % 3!= 0 or i % 5!= 0:
#             sum+=i
#     print(f"Sum of all numbers between 1 and 100 that are  not divisible by both 3 and 5 is {sum}")
# result()
# """
# To print numbers in a given pattern
# 1
# 22
# 333
# 4444
# 55555
# """
# def pattern():
#     for i in range(1,6):
#         for j in range(i):
#             print(i,end="")
#         print("")
# pattern()
# """
# To add up all the even numbers between 100 and 200
# """
# #define a function
# def sum_between_100_and_200():
#     sum=0
#     for i in range (101,201):
#         if i % 2 == 0:
#             sum+=i
#     print(f"Sum of all the even numbers between 100 and 200 is {sum}")
# sum_between_100_and_200()

# """
# To add the series of positive integers entered by the users
# excluding all the numbers that are greater than 100
# """
# def result():

# """
# To add up all the even numbers between 100 and 200
# """
# def sum_between_100_and_200():
#     sum=0
#     counter=0
#     while counter<=200:
#         if counter % 2 == 0 and counter >100:
#             sum+=counter
#             counter+=1
#     print(f"Sum of all the even numbers between 100 and 200 is {sum}")
# sum_between_100_and_200()
# """
# To solve the problem in the given program
# """
# def check():
#     product=1
#     num=float(input("Enter the first number:"))
#     while num !=0:
#         num=float(input("Enter the first number:"))
#         product=product+num
#         print("product =",product)
#     check()
# """
# To find out the largest number among the numbers entered
# by users
# """
# def largest_one(number):
#     largest_number=0
#     string=str(number)
#     for num in string:
#         if int(num) > largest_number:
#             largest_number= int(num)
#     print(f"The largest number in {number} is {num}")

# largest_one(12345)

# """
# To write a program that uses a loop to count the number
# of vowels in a given string
# """
# def count_vowels(string):
#     vowels="aeiou"
#     count=0
#     for character in string:
#         if character.lower() in vowels:
#             count+=1
#     return count

# count=count_vowels("Programming workshop")
# print("The number of vowels in the string is:",count)

# """
# To write the program that uses a loop to find the sum of
# the digits of a given number
# """
# def find_sum(number):
#     sum=0
#     string_number=str(number)
#     for num in string_number:
#         sum+=int(sum)
#     return sum

# num=int(input("Enter any number:"))
# print(f"Sum of {num} is {find_sum(num)}")
# """
# Question num 8
# """
# import random 
# #gets random number between 1 and 20
# random_number =random.randint(1,20)
# attempts_left = 10

# while attempts_left > 0:
#     guessed_number =int(input("Guess a number:"))
#     if guessed_number != random_number:
#         attempts_left -=1#reduce count if its not equal to random number
#         print(f"Incorrect guess, {attempts_left} attempts left")
#     else:
#         print(f"Your guess matches with {random_number}  ")
#         break
# """
# part 4
# """
# def add(num1,num2):
#     #take two parameters and add them
#     return num1 + num2
# def subtract(num1,num2):
#     #take two parameters and subtract them
#     return num1 -num2
# def multiply(num1,num2):
#     #take two parameters and multiply them
#     return num1*num2
# def divide(num1,num2):
#     #take two parameters and divide them
#     return num1/num2
# def modulus(num1,num2):
#     #take two parameters and find their remainder
#     return num1 % num2
# def exponentiation(num1,num2):
#     #take two parameters and find its exponentiation
#     return num1 ** num2
# def calculate():
#     while 1:
#         num1=float(input("Enter number 1:"))
#         num2=float(input("Enter number 2:"))
#         operation =input("Enter operation:\n[1:Addition]\n[2:Subtraction]\n[3:Multiplication]\n[4:Division]\n[5:Modulus]\n[6:Exponentiation]\n[q:Quit]")
#         if operation=="1":
#             print("Addition:",add(num1,num2))
#         elif operation=="2":
#             print("Subtraction:",subtract(num1,num2))
#         elif operation== "3":
#             print("Multiplication:", multiply(num1,num2))
#         elif operation=="4":
#             print("Division:", divide(num1,num2))
#         elif operation=="5":
#             print("Modulus:", modulus(num1,num2))
#         elif operation=="6":
#             print("Exponentiation:", exponentiation(num1,num2))
#         elif operation=="q":
#             print("You prompted to quit the program.")
#         else:
#             print("Invalid input")
# calculate()

# """
# Dice game program
# """
# import random 
# while 1:
#     print("Dice guesser game, press Q to exit")
#     dice_one = random.randint(1,6)
#     dice_two= random.randint(1,6)

#     guessed_value = (input("Enter your total guess value:"))
#     if guessed_value == "q":
#         break
#     guessed_value = int(guessed_value)
#     if guessed_value == dice_one + dice_two:
#         print("Congratulation, you guessed it right")
#     else:
#         print(f"Incorrect guess, correct guess was {dice_one +dice_two}")


##Question no 3
# import random

# PLAYED =0
# CORRECT_GUESS = 0

# while 1:
#     print("Dice guesser game, press q to exit")
#     dice_one = random.randint(1,6)
#     dice_two = random.randint(1,6)

#     guessed_value =input("Enter your total guess value:")
#     if guessed_value == "q":
#         win_percentage= CORRECT_GUESS/PLAYED * 100
#         print(f"You played {PLAYED} times")
#         print(f"You gueeses correct {CORRECT_GUESS} times. Your win peercentage is {win_percentage}")
#         break
#     guessed_value = int (guessed_value)
#     if guessed_value == dice_one + dice_two:
#         CORRECT_GUESS+=1
#         print("Congratulations, you guessed it right")
#     else:
#         print(f"Incorrect guess, correct guess was {dice_one +dice_two}")
#     PLAYED+=1

