# f=open("datafile.txt", "r")
# y=f.read()
# print(y)
# f.close()

# ##Question no 2
# """
# Creating a file for writing and assigning
# identifier output_file to the file
# """
# output_file=open("datafile2.txt","w")
# x=output_file.write("Hello")
# print(x)
# output_file.close()

# ##Question no 3
# """
# Checking the problem
# """
# empty_str=" "
# input_file=open("datafile.txt", "r")
# output_file=open("datafile.txt","r")
# line = input_file.readline()
# while line!=empty_str:
#     output_file.write(line + "\n")
#     line = input_file.readline()

# ##Question no 4
# """
# Checking if there is an error
# """
# input_file_opened=False
# while not input_file_opened:
#     try:
#         file_name=input("Enter file name:")
#         input_file=open(file_name,"r")
#         print(input_file.read())
#         input_file.close()
#         input_file_opened=True
#     except:
#         print("File not found")

####Part -2
##Question no 1
# def reduce_space():
#     #
#     #creating a program that reads a file and 
#     #returns the line with all extra space characters 
#     #removed """
# try:
#     f=open("character.txt","r")
#     x=f.read()
#     y=x.split(" ")
#     print(y)
#     list_1 =[]
#     for i in y:
#             list_1.append(i)
#     while("") in list_1:
#             list_1.remove("")
#     print(list_1)
#     stri=""
#     for j in list_1:
#             stri=stri +j+" "
#     print(stri)
# except:
#     print("Invalid file name")
# reduce_space()

##Question no 2
# try:
#     f=open("result.txt","r")
#     y=f.read()
#     f.close()
# except:
#     print("Invalid filename")

# def extract_temp(line):
#     x=y.split()
#     for i in x:
#         if (i.isdigit()):
#             print(i)
#         else:
#             pass
# extract_temp(y)

# ##Question no 3
# try:
#     f=open("result.txt","r")
#     x=f.read()
#     f.close()
#     print(x)
# except:
#     print("Invalid file name")
# def check_quotes(line):
#     stack=[]
#     for char in line:
#         if char in ('\'', '"'):
#             if stack and stack[-1]==char:
#                 stack.pop()
#             else:
#                 stack.append(char)
#     return not stack
# check_quotes(x)

# ##Question 4
# try:
#     f=open("result.txt")
#     x=f.read()
#     f.close()
# except:
#     print("Invalid filename")
# def count_letters(lines):
#     list1=[]
#     line=(lines.lower()).split(" ")
#     for i in line:
#         for k in i:
#             list1.append(k)
#     list2=[]
#     for j in list1:
#         y1=str(list1.count(j))
#         y2=str((j,y1)).strip("")
#         y3=j.replace(j,y2)

#         list2.append(y3)
#     list3=[]
#     list3=list(dict.fromkeys(12))
#     list4=str(list3).replace('"',"")
#     print(list4)
# count_letters(x)

# ##Question no 5
# try:
#     f=open("result.txt","r")
#     a=f.readline()
#     b=f.readline()
#     f.close()
# except:
#     print("Invalid filename")
# def interleave_chars(line1,line2):
#     a1=[]
#     b1=[]
#     for i in line1.strip("\n"):
#         a1.append(i)
#     a1.append("")
#     a1.append("")
#     for j in line2.strip("\n"):
#         b1.append(j)
#     for k in range(0,len(b1)):
#         z=a1[k] + b1[k]
#         print(z,end="" )
# interleave_chars(a,b)

##Question no 6




# ##Question no 7
# try:
#     f=open("text.txt","r")
#     a=f.read()
#     f.close()
#     print(a[0:3])
# except:
#     print("Invalid file name")

# ##Question no 8
# """
# To display True if the letter "r" appears in a 
# given month named stored in variable month
# otherwise displays false
# """
# month=input("Enter a month:")
# if("r" in month):
#     print("True")
# else:
#     print("False")


# ##Question no 9
# def count():
#     """
#     To count the number of times the letter'r' 
#     appears in a month name stored in a variable
#     """
#     month=input("Enter a month:")
#     x=month.count("r")
#     print(x)
# count()

##Question no 10
# def display():
#     """
#     To display the person's first and second name
#     in a given pattern
#     """
#     first_name=input("Enter the first name:")
#     last_name=input("Enter the last name:")
#     print(first_name, "," ,last_name)
# display()

# ##Question no 11
# def display():
#     ss_num=input("Enter social security number:")
#     new=filter(str.isdigit,ss_num)
#     new2="".join(new)
#     if (ss_num==new2):
#         print("No non-digits")
#     else:
#         print("YES,Non-digits are present")
# display()

# ##Question no 12
# def display():
#     """
#     To determine the index of @ character in an 
#     email address stored in variable
#     """
#     email_address=input("Enter email address:")
#     if ("@" in email_address):
#         index_position=email_address.index("@")
#         print(index_position)
#     else:
#         print("Not present")
# display()

##Question no 13
# def display():
#     """
#     To replace all slashes characters  present in
#     the variable date with dashes
#     """
#     date=input("Enter a date:")
#     x=date.replace("/","-")
#     print(x)
# display()

##Question no 14
# def display():
#     """
#     To display the error message without the 
#     leading and trailing asterisks and blank 
#     characters
#     """
#     err_msg=input("Enter an error message:")
#     x=err_msg.strip("*")
#     y=x.strip(" ")
#     print(y)
# display()
    
##Part-4
#Question no 1
# try:
#     f=open("text.txt","r")
#     count_lines=0
#     list=[]
#     for i in f:
#         list.append(i)
#     print(len(list))
# except:
#     print("Invalid filename")

##Question on 2
"""
To read the text file and write every other line starting
from first line to a new file
"""
try:
    f=open("text.txt","r")
    f1=open("new_text.txt","w")
    for i in f:
        f1.write(i)
    f.close()
    f1.close()
except:
    print("Invalid filename")


##Question no 3
# """
# To reads a text file and counts how many times letter
# "e" occurs
# """
# try:
#     f=open("new_text.txt","r")
#     list=[]
#     for i in f:
#         list.append(i)
#     list1=str(list).strip("\n")
#     count=0
#     for j in list1:
#         for k in j:
#             if (k=="e"):
#                 count+=1
#     f.close()
#     print("The number of times e is present in the file is:",count)
# except:
#     print("Invalid filename")

##Question no 4
# """
# To reads a text file containing numerical expressions on each line and
# print them oout along with the results
# """
# try:
#     f=open("new_text.txt","r")
#     list=[]
#     for i in f:
#         for j in i:
#             list.append(j)
#     sum=int([0]) + int(list[2])
#     print(sum)
# except:
#     print("Invalid filename")
