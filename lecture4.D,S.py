# LECTURE 4 
# Dictionary & Set

# Dictionary *******************************

# info = {
# "name" : "Tarun Patidar",
# "subjects" : ['pythhon' , 'jawa'  ],
# "age" : 19, 
# "marks" : (90 , 85)
# }
# info["name"] = "shradha" # overwrite
# info["semester"] = "3rd" # to add some value's
# print(info) 

# Nested dictionary

# A = { 
# "name" : "tarun",
# "sub" : ["python" , "jawa" , "AI.ML"],
# "marks" : {
#     "python" : 95,
#     "jawa" : 84,
#     "AI.ML" : 89
# },
# "age" : 19
# }
# print(A)
# print(A["name"])
# print(A["marks"])
# print(A["marks"]["python"])

# Set ***************************

# set is the collection unorderd items.
# each element in the set must be unique & unmutable.

# nums = {1, 2, 3, 4}
# set2 = {1, 2, 2, 2, 2} # repeated element store only once , so it resolved to {1, 2}.
# null_set = set() # empty set syntex.

# setA = {1, 2, 2, 2, "hello", "india", "hello"} # duplicate values are ignored.
# print(setA).
# print(len(setA)) # valid.
# print(type(setA)) # valid.

# empty set.

# A.add(el) # to add element.
# A.remove(el) # to remove element.
# A.clear() # empties the set.
# A.pop() # select a random value from set.
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add("hello")
# collection.add("india")
# collection.remove(2)
# collection.add((1, 2, 3, 4))
# collection.add([1, 2, 3, 4]) # the list is unusable in set
# collection.add(input("enter your name : "))
# print(collection)

# Aset = {14, 3, 5, 7, 9}
# Bset = {7, 4, 6, 5, 1}
# print(Aset.union(Bset)) 
# print(Aset.intersection(Bset)) 

# dictionary = {
#     "cat" : "cat is a familier amimal",
#     "table" : {"plastic table" , "wood table"}
# }   
# print(dictionary)

# # # question 

# marks = {}
# x = float(input("enter phy marks : "))
# marks.update({"phy" : x})
# x = float(input("enter math marks : "))
# marks.update({"math" : x})
# x = float(input("enter chem marks : "))
# marks.update({"chem" : x})
# print(marks)

