from math import*
print("Hello World")
print("You are most welcome to Rhodes Island Sir. It is a very beautiful place")
#variables and data types
#variables: changable values in code 
character_name = "John"
character_age = "35"
character_home = "Bucharest"
print("My name is " + character_name + " I am " + character_age + " years old and i live in " + character_home + ", Romania." )
#data types 
# Strings; these allow us to store plain text data
print("Girraffe Academy")
#new line 
print("Girraffe\nAcademy")
print("\"Girraffe\" \"Academy\"")
name = "Sharif"
print("Hello " + name ) # concatinating strings 
zoo = "Giraffe Academy"
# converting text in a string  to upper or lower case 
print(zoo.upper())
print(zoo.lower())
#checking if text in a string is upper or lower case. it either returns True or False 
print(zoo.islower())
print(zoo.isupper())
print(zoo.upper().isupper()) #converted it to upper case first so it returned true after 
print(zoo.lower().islower()) #converted it to lower case first so it also returned true 
#length of a string 
print(len(zoo))
print(zoo[3])
print(zoo.index("G"))
print(zoo.replace("Giraffe", "Elephant"))
#Numbers
x = 5
y = 6
xx = (x + y)
print(xx)
yy = xx - 2
print(yy)
zz = x * y 
print(zz)
# functions with numbers 
print(abs(-25))
print(pow(3,3))
print(round(5.55))
# other functions that need importing files 
print(floor(5.55))
print(floor(-5.55))
print(ceil(5.55))
print(ceil(-5.55))
# square root function
print(sqrt(81))
#getting user input in python 
Name = input("Enter your name: ")
print("Your name is " + Name )
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 + num2 
print(result)
# lists in python 
lucky_numbers = [1,2,3,4,5]
friends = ["Jenny", "Ketty", "Kai", "Rakai"]
print(lucky_numbers)
print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])
# list Functions 
#friends.extend(lucky_numbers)
print(friends)
lucky_numbers.append(6)
print(lucky_numbers)
friends.insert(1, "Shary")
print(friends)
friends.remove("Shary")
print(friends)
friends.pop()
print(friends)
jambled_Numbers = [23,45,667,12,3,46,32]
# sorting a list in ascending order 
jambled_Numbers.sort()
print(jambled_Numbers)
# tuples; these have their values  constant and unchangable
coordinates = (4,5,6,7)
print(coordinates)
#functions 
# normal ones 
def say_hi(): # declaration of the function 
    print("Hello User")
say_hi() # calling the function 
def say_hello(name):
    print("Hello " + name)
say_hello("Sharif")
#return Statement
def cube(nums): # this function returns the cube of a number 
    result = nums * nums * nums
    return result 
r = cube(5)
print(r)
# control flow statements 
# if statements 
is_male = False
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif not is_male and is_tall:
    print("You are a tall female")
elif not is_tall and is_male:
    print("You are a short male")
else:
    print("You are a short male")
# while loops
i = 0
while i <= 10:
    print(i)
    i = i + 1
for i in range(10):
    print(i)
# iterating through lists and strings 
river = "River Nile"
River = []
k = 0
while k < len(river):
    River.append(river[k])
    k += 1
print(River)
x = "12345678890"
numbers = []
j = 0
while j < len(x):
    numbers.append(x[j])
    j += 1
print(numbers)
