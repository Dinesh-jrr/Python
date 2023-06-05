
# #Error handling
# print("start")
# try:
#     print(2/0)
# except ZeroDivisionError:
#     print("Error")
# print("End")

# #Example
# try:
#     numerator=10
#     denominator=0
#     result=numerator/denominator
#     print(result)
# except ZeroDivisionError:
#     print("Error:Denominator cannot be 0.")

##function calling
# try:
#     user_input=int(input("Please enter a number:"))
#     result=10/user_input
#     print(f"The result is:{result}")
# except ValueError:
#     print("Invalid input:please enter a number")
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# def divide(x,y):
#     if y==0:
#         raise ValueError("Error")
#     return x/ y
# try:
#     result=divide(10,0)
#     print(result)
# except ValueError as e:
#     print(e)



