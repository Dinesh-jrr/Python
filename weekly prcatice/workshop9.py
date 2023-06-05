# def basic_operation():
#     """
#     A python function that prompts the user two integers and 
#     then divides the first integer by the second integer.
#     Handle any exceptions that may occur during the division
#     operation
#     """
#     first_number=input("Enter the first number:")
#     second_number=input("Enter the second number:")
#     if not first_number.isdigit() or not second_number.isdigit():
#         print("Please enter a valid number")
#         return
#     try:
#         result=int(first_number) / int(second_number)
#         print(f"Result is {result}")
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
#     except Exception as e:
#         print(f"An error occured{e}")
# basic_operation()

##Question no 2
# def file_read_error():
#     """
#     A python function that reads a file name from the user and attempts to open the file.
#     Handle any exceptions that may occur if the file doesnot exist or if there is an error
#     reading the file
#     """
#     filename= input("Enter the file name:")
#     try:
#         with open(filename) as f:
#             for line in f:
#                 print(line)
#     except FileNotFoundError:
#         print("File not found")
#     except Exception as e:
#         print(f"An error occured{e}")
# file_read_error()

###Question no 3
# def average_calculator():
#     """
#     Python function that prompts the user to enter a list of numbers and calculate the
#     average of those numbers.Hande an exceptions that may occur if any user enters
#     non-numeric values.
#     """
#     numbers=[]
#     while 1:
#         number=input("Enter a number:")
#         if number == "q":
#             break
#         try:
#             numbers.append(int(number))
#         except ValueError:
#             print("Please enter a valid number")
#     try:
#         average=sum(numbers)/len(numbers)
#         print(f"Average is{average}")
#     except ZeroDivisionError:
#         print("Enter atleast one number")
#     except Exception as e:
#         print(f"An error occured {e}")
# average_calculator()

##Question no 4
# import random
# def guesser():
#         """
#         A pythonn function that generates a random number between 1 and 10 and prompts the to
#         guess the number.Handle any exceptions that may occur if the user enters non-numeric
#         values or if the guess is out of range
#         """
#     random_num=random.radint(1,10)
#     while 1:
#          guess_num=input("Guess the number:")
#         if guess_num == "q":
#             break
#         try:
#             guess_num=int(guess_num)
#             if guess_num > 10 or guess_num < 1:
#                 print("Please enter a number between 1 and 10")
#                 continue
#             if guess_num == random_num:
#                 print("You guessed it right")
#                 break
#             print("You guessed it wrong")
#         except ValueError:
#             print("Please ente a valid number")
#         except Exception as e:
#             print(f"An error occured{e}")

# guesser()

##Question no 5
# def sum_of_list():
#     """
#     A function that prompts the user to enter a list of integers and then calculates the
#     sum of those integers.Handle any exceptions that may occur if the user enters 
#     non-numeric values.
#     """
#     numbers=[]
#     while 1:
#         number=input("Enter a number:")
#         if number == "q":
#             break
#         try:
#             numbers.append(int(number))
#         except ValueError:
#             print("Please enter a valid number")
#     try:
#         total = sum(numbers)
#         print(f"Total is {total}")
#     except Exception as e:
#         print(f"An error occured{e}")
# sum_of_list()

##Question no 6
# def zero_division_error_handling():
#     """
#     Using try_except, showcase the ZeroDivisionError
#     """
#     first_number=input("Enter the first number:")
#     second_number=input("Enter the second number:")
#     if not first_number.isdigit() or not second_number.isdigit():
#         print("Please enter a valid number")
#         return
#     try:
#         result=int(first_number) / int(second_number)
#         print(f"Result is {result}")
#     except ZeroDivisionError:
#         print("Cannot divide by zer0")
#     except Exception as e:
#         print(f"An error occured{e}")
# zero_division_error_handling()

##Question no 7
# def index_error():
#     """
#     A simple list containing five elements and try to print the 
#     sixth element of the list.(use IndexError exception)
#     """
#     list=[1,2,3,4,5]
#     try:
#         print(list[5])
#     except IndexError:
#         print("Index out of string")
#     except Exception as e:
#         print(f"An error occured{e}")
# index_error()

##Question no 8
# def name_error():
#     """
#     This function handles undeclared variables
#     """
#     first_name="DineshJr"
#     print("First name is:",first_name)
#     try:
#         print("Last name is :",last_name)
#     except NameError:
#         print("Last name is not defined")
#     except Exception as e:
#         print(f"An error occured{e}")
# name_error()

##Question no 9
# def try_else_showcase():
#     """
#     Divide two numbers and return the result.
#     Handle exception if y is zero
#     """
#     first_number = input("Enter the fist number:")
#     second_number=input("Enter the second number:")
#     if not first_number.isdigit() or not second_number.isdigit():
#         print("Please enter a valid number")
#         return
#     try:
#         division=int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("Error:division by zero")
#     else:
#         print("Division successful.")
#         return division
# try_else_showcase()

##Question no 10
# def custom_exception_showcase():
#     """
#     Raise Valueerror if the input is not a number
#     """
#     first_number=input("Enter the first number:")
#     second_number=input("Enter the second number:")
#     if not first_number.isdigit() or not second_number.isdigit():
#         raise ValueError("Please enter a valid number")
# custom_exception_showcase()

######Part 3
#Question no 1
# def string():
#     """
#     Python function that prompts the user to enter a string and then
#     convert it to an integer.Handle the ValueError exception that 
#     may occur if the string cannot be converted to an integer
#     """
#     num=input("Enter any number:")
#     try:
#         num=int(num)
#     except ValueError:
#         print("Invalid number")
#     print(type(num))
# string()

##Question no 2
# def divide():
#     numerator=input("Enter the numerator:")
#     denomonator=input("Enter the denomonator:")
#     try:
#         result=int(numerator) / int(denomonator)
#         print(f"Result is {result}")
#     except ValueError:
#         print("Cannot perform division on non-numeric values")
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
#     except Exception as e:
#         print(f"An error occured :e")

# divide()

##Question no 3
# def check():
#     amount=input("Enter the amount:")
#     try:
#         if int(amount) < 10000:
#             raise ValueError("Amount should be greater than 10000")
#     except ValueError as e:
#         if "Amount should be greater than 10000" in str(e):
#             print(e)
#         else:
#             print("Invalid number")
#     else:
#         print("Amount is:", amount)
# check()

##Question no 4
# def check():
#     try:
#         text=input("Enter any number:")
#         print(text)
#     except EOFError:
#         print("End of file reached")
# check()

##Question no 5
# def take(list):
#     try:
#         return max(list)
#     except ValueError:
#         print("List is empty")
#     except TypeError:
#         print("List contains non-numeric values")
# print(take([1,2,3,4,5,"a"]))

##Question no 6
# def check(list):
#     try:
#         return max(list)
#     except ValueError:
#         print("List is empty")
#     except TypeError:
#         print("List contains non numeric values")
# print(check([]))

##Question no 7
# def value(dict,key):
#     try:
#         return dict[key]
#     except KeyError:
#         print("Key is not found")
#     except Exception as e:
#         print(f"An error occured {e}")

# print(value({'a':1,'b':2},'c'))

##Question no 8
# def concate(str1,str2):
#     try:
#         return str1 + str2
#     except TypeError:
#         print("One of the value is not string")
# print(concate("1",2))
# print(concate("1","2"))
