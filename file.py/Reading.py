##  Reading the content of file.
##  In this code we have to give the closing tag.
f = open("world.txt" , "r")
content = f.read()
print(content)
f.close

##             (AND)            ##
## This is for skipping closing tag.

with open("world.txt","r") as f:
    content = f.read() 
    print(content)

