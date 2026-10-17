# Chapter 2 
# String & conditional Statement's ************

# str1 = "This is a string concatenation example."
# str2 = "this is a second string that will be concatenated."
# print(str1 + " " + "\n" + str2)
# ??
#\n Escape Sequance Character (ESC) used for print in next line
# \t Tab

########################

#STRING

# string is data type that stores a sequence of character

# Basic Operators
# 1. Concatenation
# "hello" + "world" = "helloworld"

# 2. length of string
#len(str)
# EX
# name = "tarun"
# print(len(name)) 
# output will be 5

# INDEXING

# tarun_ptdr
# 12345678910 

# str = "tarun"
# print(str[0]) #ouput > #t
# print(str[0:5]) [0:len(str)] # outout > tarun

# slicing
# negative index 
# t a r u n 
#-5-4-3-2-1
# str = "tarun"
# print(str[-4:]) output > arun

# STRING FUNCTION

# str = "trade with tarun"

# print(str.endswith("un")) # output > True
# print(str.startswith("with")) # uutput > False
# print(str.capitalize()) # output > Trade with tarun
# print(str.upper()) # output > TRADE WITH TARUN
# print(str.lower()) # output > trade with tarun
# print(str.replace("tarun", "tarun_ptdr")) # output > trade with tarun_ptdr
# print(str.split()) # output > ['trade', 'with', 'tarun']
# print(str.find("with")) # output > 6

# main functions of string
# endswith("word")
# capitalize("container")
# replace("old", "new")
# find(word)
# count("word")

# print(len(input("Enter your name: ")))
# word = ("i am a senior global financial $ marcket risk $ asesment and management professional $ with 10 years of experience $ in risk management, financial marcket risk asesment, and financial marcket risk management.")
# print(word.count("$"))
# name = input("enter your name: ")
# print("length of your name is: ", len(name))

# CONDITIONAL STATEMENTS

# if()
# elif()
# else()

# EXAMPLE

# light = ("red")
# if(light == "red"):
    # print("stop") # the space before print is called (indentation) and it is very important in python.
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("wait")
# else:
#     print("light is broken")

# print("end of code")

# every condition have to start by if and then elif and then else.

# age = int(input("enter your age : "))
# if(age>=18):
#     print("you have rights to vote.")
# else:
#     print("You are not an adult.")

# marks = (int(input("Enter student marks: ")))
# if(marks>=90):
#     grade = "A"
# elif(70<=marks<90):
#     grade = "B"
# elif(50<=marks<70):
#     grade = "C"
# elif(30<=marks<50):
#     grade = "D"
# else:
#     grade = "Fail"

# print("The student's grade is:", grade)

# name = input("Enter your name: ")
# print("Hello,", name)
# marks = int(input("enter your marks: "))
# if(marks>=90):
#     grade = "A & CGPA is 10"
# elif(70<=marks<90):
#     grade = "B & CGPA is 7"
# elif(50<=marks<70):
#     grade = "C & CGPA is 5"
# elif(30<=marks<50):
#     grade = "D & CGPA is 3"
# else:
#     grade = "Fail & CGPA is 0"
# print("Hey" , name, "Your grade is:", grade)

# age = float(input("Enter your age: "))
# if(age>=18):
#     if(age>=70):
#         print("You are a senior citizen, you are unable to drive.")
#     else:
#         print("You are able to drive.")
# else:
#     print("cannot drive")

# a = int(input("Enter a first number: "))
# b = int(input("Enter a second number: "))
# c = int(input("Enter a third number: "))
# if(a>b and a>c):
#     print("a is the greatest number")
# elif(b>a and b>c):
#     print("b is the greatest number")
# else:
#     print("c is the greatest number")

# no = int(input("enter a number: "))
# if(no % 2 == 0):
#     print("The number is even.")
# else:
#     print("The number is odd.")

# LECTURE 2 ENDS HERE

