from math import*
# printing text from python
print("Hello World")
# variables and data types
name = "John"
age = "35"
village = "Kawempe"
school = "Old Kampala SSS"
print("My name is " + name + " and i am "+ age + " years old. I stay in " + village + ", and I study from " + school)
# Data types 
# strings 
name = "sharif"
print(name)
# escape sequences 
print("Giraffe\nAcademy")
print("\"Giraffe\" \"Academy\"")
greet = "HEllo"
print(greet + " there")
print(greet.upper())
print(greet.lower())
print(greet.upper().isupper())
print(greet.lower().islower())
print(greet.islower())
print(len(greet))
print(greet[1])
print(greet.index("H"))
print(greet.replace("E", "e"))
# Numbers 
print(5%2)
x = 6
y = 7
z = 2
sum = x + y
print(sum)
divide = sum / z
print(divide)
print("I am " + str(divide))
print(abs(-45))
print(pow(5,2))
print(round(5.5))
print(floor(5.5))
print(ceil(5.5))
print(sqrt(64))
# list in python 
my_friends = ["Jony", "Kenny", "Liam", "shary"]
print(my_friends)
numbers = [1,2,3,4,5,6,7,8,9,10]
letters = ["a", "b", "c", "d", "e"]
# adding two lists together 
numbers.extend(letters)
print(numbers)
# appending elements to a list
my_friends.append("Drake")
print(my_friends)
# inserting elements to a list 
my_friends.insert(3, "Sharon")
print(my_friends)
# removing elements from a list 
my_friends.remove("shary")
print(my_friends)
# removing the last element from a list
my_friends.pop()
print(my_friends)
# sorting elements in a list 
my_friends.sort()
print(my_friends)

# tuples 
coordinates = {4,-17} # these are always constant through out and they can never be modified 
print(coordinates)

# functions 
# functions with out return statements 
def say_hi():
    print("Hi user")


say_hi()
# with parameters 
def Say_Hello(Name):
    print("Hello " + Name)

Say_Hello("Jorum")

# functions with return statements 

def Cube(num):
    result = num * num * num
    return result 
print("The cube of 2 is " + str(Cube(2)))

# control statements 
# if statements 
is_Male = False 
is_tall = False
if (is_Male and is_tall):
    print("You are a tall male")
elif (is_Male and not is_tall):
    print("You are a short male")
elif (not is_Male and is_tall):
    print("You are a tall lady")
else:
    print("You are a short lady")

# while loops
i = 0 
while (i < 10):
    print(i)
    i = i +1

# for loops 
for j in range(10):
    print(j)

## thanks done for the first part of my practice 
# dictionaries have keys and values 
#some dictionary functions 

capitals = {"USA": "Washington DC",
            "Uganda": "Kampala",
            "Kenya": "Nairobi",
            "France": "Paris",
            "Romania": "Bucharest"}
print(capitals.get("Romania")) # gets the value to a key input in the function
# to add items to the dictionary
capitals.update({"Germany": "Berlin"})
print(capitals)
# to remove a certain item 
capitals.pop("France")
print(capitals)
# to remove the last item 
capitals.popitem()
print(capitals)

# to print all the keys 
kk = capitals.keys()
print(kk)
# iterating through the keys 
for k in kk:
    print(k)
# tp print all the values of the dictionary 

vv = capitals.values()
print(vv)
# iterating through the values 

for v in vv:
    print(v)

# to get all the items from a dictionary and iterate through them using a for loop 

items = capitals.items()

for keys, values in items:
    print(f"{keys}: {values}")
    







