# Chapter 2 String & conditional Statements ************

# str1 = "This is a string concatenation example."
# str2 = "this is a second string that will be concatenated."
# print(str1 + " " + "\n" + str2)
# ??
#\n Escape Sequance Character (ESC) used for print in next line
# \t Tab

########################

#STRING #####################################

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
# print(str[0]) ouput > 
# print(str[0:5]) [0:len(str)] outout > tarun

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
# print(str.split(" ")) # output > ['trade', 'with', 'tarun']
# print(str.find("with")) # output > 6

# main functions of string
# endswith("word")
# capitalize()
# replace("old", "new")
# find(word)
# count("word")

# print(len(input("Enter your name: ")))
# word = ("i am a senior global financial $ marcket risk $ asesment and management professional $ with 10 years of experience $ in risk management, financial marcket risk asesment, and financial marcket risk management.")
# print(word.count("$"))
# name = input("enter your name: ")
# print("length of your name is: ", len(name))

# CONDITIONAL STATEMENTS
