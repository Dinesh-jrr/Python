#Question no.1
 #def create():
#     """
#     To write a program that create a lists of integers and 
#     append new integer to end of the list
#     """
#     list= [1,2,3,4,5]
#     print(list)
#     list.append(6)
#     print(f"The list after adding a number is:", list)
# create()

# #Question no 2
# def create():
#     """
#     To create a nested list of strings and print the 
#     first element of the second list
#     """
#     list=[["Dinesh","Rohan","Dipesh"],["Messi","Ronaldo","Neymar"]]
#     print(list[1][0])
# create()

## Question no 3
# def create():
#     """
#     To create a tuple of integers and print the length of
#     the tuple
#     """
#     number=(1,2,3,4,5,6,7,8,9)
#     print(len(number))
# create()

# ## Question no 4
# def create():
#     """
#     To create set of integers and then add a new integer to
#     the set
#     """
#     set={1,2,3,4}
#     print(f"Original set:",set)
#     set.add(5)
#     print(f"Updated set:",set)
# create()

# ##Question no 5
# def create():
#     """
#     To create a dictionary of student names and their corresponding
#     ages and then print the age of a specific student
#     """
#     student={"Messi":37,"Ronaldo":39,"Neymar":29}
#     print(student["Messi"])
# create()

# ##Question no 6
# def write():
#     """
#     To prompt the user for a list of integers and
#     stores them in a list
#     """
#     list=[]
#     while True:
#         number=input("Enter a number:")
#         if number == "q":
#             break
#         else:
#             number = int (number)
#             if number > 100:
#                 list.append("Over")
#             else:
#                 list.append(number)
#     print(list)
# write()

## Question no 7
# def write():
#     """
#     write a programa
#     """
#     num_list =[]
#     num_input  = input("Enter a list of integers:")
#     num_list = num_input.split()
#     num_list = [ for num in num_list]
#     num_list =["over" if num > 100 else num for num in num_list]
#     print("The resulting list is :", num_list)
# write()

# ## Question no 7
# def add_daily_temp(temperature_dict,temperature,day):
#     """
#     Takes in a dictionary, a temperature and a day of the 
#     week and add the temperature to the dictionary if it does
#     not already contain a temperature for that day.
#     If the temperature for that  day is already present in 
#     the dictionary, returns the dictionary
#     """
#     if day not in temperature_dict:
#         temperature_dict[day]= temperature
#     return temperature_dict
# date ={"Monday": 20, "Tuesday":50}
# print(add_daily_temp(date, 40 , "Monday"))
# print(add_daily_temp (date,40, "Wednesday"))

 ##Question no 8
# def create():
#     """   
#     To concatenate the dictionaries and create a new one
#     """
#     dict1={1:10,2:20}
#     dict2={3:30,4:40}
#     dict3={5:50,6:60}
#     dict={}
#     for i in (dict1,dict2,dict3):
#         dict.update(i)
        
#     print(dict)
# create()


###Question no 9
# def insert_string(list,string):
#     """
#     Take a list and add string from string parameter to each
#     element
#     """
#     new_list = [string + str(element) for element in list]
#     return new_list
# list=[1,2,3,4]
# string= "emp"
# print(insert_string(list,string))

##Question no 9
# def display():
#     items={"item1":45.50,"item2":35,"item3":41.30, "item4":55, "item5":24}
#     #sort all the values from biggest to small
#     values_list = list(items.values())
#     values_list.sort(reverse=True)
#     top_3_numbers = values_list[:3] #take top three numbers
     
#      #reversing the items dictionary so that it becomes value:key
#      # e.g {45.50:"item1"}
#     reversed_items={}
#     for item in items:
#         value = items[item]
#         reversed_items[value] = item

#     for number in top_3_numbers:
#         key = reversed_items[number]
#         value= number
#         print(key , ":", value)
# display()

# ##Question no 10
# def display():
#      students =[
#         {"student_id":1, "name":"Jean Castro" , "class":"V"},
#         {"student_id":2, "name":"Lula Powell", "class":"V"},
#         {"student_id":3, "name":"Brian Howell", "class":"VI"},
#         {"student_id":4, "name":"Lynne Foster", "class":"VI"},
#         {"student_id":5, "name":"Zachary Simon", "class":"VII"}

#     ]
#      key = input("Enter key to search:")
#      value = input("Enter value to search:")
#      key_found = False
#      value_found = False
#      for student in students:
#           if key in student:
#                key_found= True
#           if value in list(student.values()):
#                value_found = True
#      if key_found:
#           print(f"Key {key} exists")
#      else:
#         print(f"Key {key} doesnot exist")
# display()

##Question no 11
# def display():
#     """
#     To takes list of strings and return a new list with only
#     the strings that contains the letter "a"
#     """
#     strings=[]
#     while 1:
#         string= input("Enter any string:")
#         if string == "q":
#             break
#         strings.append (string)
    
#     print("List of strings:", strings)
#     filtered_list = [string for string in strings if "a" in string.lower()]
#     print("List of strings with a in it:", filtered_list)
# display()

 ##Question no 2 
# def display( list_of_people):
#     """
#     To take a list of dictionaries representing people with their age,
#     and returns aa new list of dictionaries with only the people over
#     the age of 18
#     """
#     age_filtered=[]
#     for people in list_of_people:
#         if people ["age"] > 18:
#             age_filtered.append(people)
#     return age_filtered
# lists=[{"name":"Dinesh","age":21},
#             {"name":"Neymar","age":29},
#             {"name":"Messi","age":37},
#             {"name":"Ronaldo","age":39}]
# filtered_list=display(lists)
# print(filtered_list)

##Question no 3
# def set(set1,set2):
#     """
#     To take two sets and return a set of common elements
#     """
#     return set1.intersection(set2)
# set1= set()
# set2= set()
# while 1:
#     num=input("Enter any number for set 1:")
#     if num== "q":
#         break
#     set1.add(int(num))
# while 1:
#     num1=input("Enter any number for set 2 :")
#     if num1=="q":
#         break
#     set2.add(int(num1))
# print("Set 1:",set1)
# print("Set 2:",set2)
# print("common elements:",set(set1,set2))

##Question no  4
# def vowel(string):
#     """
#     To take in a string and returns True if the string starts with
#     a vowel
#     """
#     vowels="aeiou"
#     if string[0].lower() in vowels:
#         return True
#     return False
# sets = set()
# while True:
#     string=input("Enter a string:")
#     if string == "q":
#         break
#     else:
#         sets.add(string)
# filtered_sets={string for string in sets if vowel(string)}
# print(filtered_sets)

##Question no 5
# list=[10,11,12,13]
# def convert_to_string(list):
#     """
#     To take in a list of integers and returns a single integer
#     """
#     string=""
#     for number in list:
#         string+= str(number)
#     return int(string)
# print(convert_to_string(list))

##Question no 6
# def average_temp(temperature_dict):
#     """
#     To take in a dictionary of daily temperatures and returns the average temperature
#     over the weekend for the weekly temperature given 
#     """
#     weekend=["Sunday","Monday"]
#     total=0
#     for day in weekend:
#         total += temperature_dict[day]
#     return total /len(weekend)

# data={"Sunday":60,"Monday":70,"Tuesday":40,"Wednesday":20,"Thursday":30,"friday":10,"saturday":50}
# print(average_temp(data))




    




    