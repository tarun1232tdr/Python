# GPT stands for Generative Pre-trained Transformer

# area of circle
# area of circle is pi(r*r)
# pi = 3.14
# r = float(input("enter radius of circle : "))
# area = (pi*r*r)
# print(area)

# aerea of rectangle
# area of rectangle is length * width
# length = float(input("enter length of rectangle : "))
# width = float(input("enter width of rectangle : "))
# Area_of_rectangl = (length * width)
# print(Area_of_rectangl)

# area of triangle
# area of triangle is base * height / 2
# base = float(input("enter the base of triangle : "))
# height = float(input("enter the height of triangle : "))
# print(base*height/2)

# # Define your initial value and the percentage you want to add
# original_value = 100
# percentage_to_add = 20  # represents 20%

# # # Calculate the new value
# new_value = original_value * (1 + percentage_to_add / 100)

# print(new_value)  # Outputs: 115.0

# initial_capital = 100000
# profit_1year = 50

# new_capital = initial_capital*(profit_1year/100)
# print(new_capital)

# A = float(input("Enter your capital : "))
# B = float(input("Enter accpected return per year : "))
# C = A*(B/100)

# print(C)

# A = float(input("enter value of A : "))
# B = float(input("enter value of B : "))
# A,B=B,A
# print("A=",B ,"B=",A)

# tarun = {
#     "Name" : "Tarun Patidar",
#     "Address" : "Indore",
#     "Occupation" : "Student",
#     "Studies" : "2ndyear",
# }
# tarun["Name"] = "shradha"
# tarun["Studies"] = "BCA 2nd year"
# print(tarun)

# A = float(input("Enter a value : "))
# B = float(input("Enter percent to find : "))
# c = A*(B/100)
# print(c)

# list

# A = ["tarun", 1232, "patidar" , "indore"]
# A[0] = "student" # to replace value of a specific index.
# # print(A[1])
# # print(A[0])
# print(len(A))

# username = input("enter username : ")
# password = input("enter password : ")
# if username == "smith" or password == "tiger":
#     print("welcome")
# else :
#     print("bye")

# aadharcardno = input("enter your aadhar card no : ")
# pancardno = input("enter your pan card no")
# if aadharcardno == "123123" or pancardno == "123123":
#     print("welcome")
# else :
#     print("eror")


# aadharcardno = input("Enter your Aadhar card no: ")

# if aadharcardno == "123123":
#     print("Welcome")
# else:
#     pancardno = input("Enter your PAN card no: ")
#     if pancardno == "123123":
#         print("Welcome")
#     else:
# #         print("Error")

# A = float(input("enter a no : "))
# if A % 2 == 0:
#     print("the no is even")
# else:
#     print("the no is odd")

# A = float(input("enter a no : "))
# if A % 2 == 0:
#     print("the no is even")
# else:
#     print("the no is odd")

# **************
# 1000000000000001 is odd
# 10000000000000001 is even 

# A = float(input("enter value of A : "))
# B = int(input("enter value of B : "))
# D = int(input("enter value of D : "))
# C = int(input("enter value of C : "))
# A,B,C,D = D,C,B,A
# print("value of A : ",A)
# print("value of B : ",B)
# print("value of C : ",C)
# print("value of D : ",D)

# # Result of students 

# maths = float(input("enter maths marks : "))
# eng = float(input("enter eng marks : "))
# hindi = float(input("enter hindi marks : "))
# physics = float(input("enter physics marks : "))
# chemistry = float(input("enter chemistry marks : "))
# per = 100*(maths + eng + hindi + physics + chemistry)/500
# if  maths < 33:
#     print("supply in maths")
# if eng < 33:
#     print("supply in eng")
# if hindi < 33:
#     print("supply in hindi")
# if physics < 33:
#     print("supply in physics")
# if chemistry < 33:
#     print("supply in chemistry")
# if chemistry < 33 and physics < 33 and maths < 33 and eng < 33 and hindi < 33:
#     print("you get supply in every subject")
# elif maths > 100 or eng > 100 or hindi > 100 or physics > 100 or chemistry > 100:
#     print("your any subject marks can'not be : > 100")
# elif per>=60 and per<=100 and maths >= 33 and hindi >=33 and eng >=33 and physics >=33 and chemistry >=33:
#     print("1st dividion , Grade='A'" ,", your percentage are : ", per)
# elif per<60 and per>=40  and maths >= 33 and hindi >=33 and eng >=33 and physics >=33 and chemistry >=33:
#     print("2nd division , Grade='B'" , ", your percentage are : ", per)
# elif per<40 and per>=33  and maths >= 33 and hindi >=33 and eng >=33 and physics >=33 and chemistry >=33:
#     print("3rd division , Grade='C'" , ", your percentage are : ", per)
# else :
#     print("fail")


# to see the no you enter is even or odd , and positive or negative.

# no = float(input("enter any number : "))
# if no>=0 and no%2==0:
#     print("Given no is even")
# if no>=0 and no%2!=0:
#     print("Given no is odd")
# if no>=0:
#     print("Given no is positive")
# if no<0:
#     print("Given no is negative")

# to find net price of something you buy.

# price = float(input("Enter item price : "))
# qty = float(input("Enter quantity of item : "))
# net_price = price*qty
# if net_price<=1000:
#     print("your discount on net price is :", (net_price*10)/100, "$"  , "# final price to pay is : ", net_price-(net_price*10)/100, "$")
# elif net_price>1000 and net_price<=2000:
#     print("your discount on net price is :", (net_price*20)/100, "$"  , "# final price to pay is : ", net_price-(net_price*20)/100, "$")
# elif net_price>=2000:
#     print("your discount on net price is :", (net_price*30)/100, "$"  , "# final price to pay is : ", net_price-(net_price*30)/100, "$")
# if net_price<=0:
#     print("Error")

# given no is vovel or not.

# ch = str(input("enter any veriable : "))
# if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
#     print("vovel")
# else :
#     print("Not a vovel")

# username = str(input("Enter your username : "))
# password = int(input("Enter your password : "))
# if username == "Tarun" and password == 1232:
#     print("welcome tarun.")
# elif username != "Tarun" and password == 1232:
#     print("username incorrect.")
# elif username == "Tarun" and password != 1232:
#     print("password is invalid.")
# # else :
# #     print("password and username is invalid .")

# no = 5
# while  50>=+no>=0 :
#     print(no)
#     no+=5

## to reverse any number.

# n = 3475
# t = 0
# # while n != 0:
# #    r = n%10
# #     t = t*10+r
# #     n = n//10
# #  print(t)

# number = 123456789
# count = 0
# if number == 0:
#     count = 1
# else:
#     number = abs(number)
    
#     while number > 0:
#         count += 1
#         number = number // 10 

# print("Total Number of Digits:", count)


# with open("data.txt","r") as f1:
#     with open("copy.txt","w") as f2:
#         for line in f1_txt:

with open('first.txt', 'r') as f1, open('second.txt', 'w') as f2:
    for line in f1:
        f2.write(line)
print("file has been copied.")

