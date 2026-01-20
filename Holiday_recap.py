from math import*
print("hello World")
# variables 
character_name = "John"
character_home = "Bucharest"
character_age = 35
print("My name is " + character_name + " i live in " + character_home + " i am " + str(character_age) + " years old.")
# different Data types 
#Strings 
print("Hello")
print("Giraffe\nAcademy")
print("\"Giraffe \"Academy\"")
name = "Sharif"
print(name)
print("Hello there " + name )
zoo = "Giraffe Academy"
print(zoo.lower())
print(zoo.upper())
print(zoo.isupper())
print(zoo.lower().islower())
print(len(zoo))
print(zoo[0])
print(zoo.index("G"))
print(zoo.replace("Giraffe", "Lion"))
#Numbers
x = 5 
y = 6
print(x + y)
print(5 % 2)
print(abs(-2))
print(pow(5,2))
print(round(5.55))
print(floor(5.55))
print(ceil(5.55))
print(sqrt(64)) # for getting the square root 
name = input("Enter your names please: ")
print("Hello there " + name + " how are you doing")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = num1 + num2 
print(result)
#Lists in Python; collections of data in python
lucky_numbers = [1,2,3,4,5,6]
print(lucky_numbers)
print(lucky_numbers[0])
print(lucky_numbers[-1])

print(lucky_numbers[2:])
print(lucky_numbers[2:3])
# List Functions 
food = ["beef", "chicken", "pizza","Tomato"]
food.extend(lucky_numbers)
print(food)
friends = []
friends.append("Ham")
friends.append("John")
friends.append("jenny")
friends.append("Lewis")
print(friends)
friends.insert(1, "Kenny")
print(friends)
friends.remove("Kenny")
print(friends)
friends.pop()
print(friends)
print(friends.index("Ham"))
jambled_numbers = [2,45,6,78,99,12,1,34]
jambled_numbers.sort()
print(jambled_numbers)
# Tuples 
coordinates = (1,2,3,4,5)
print(coordinates)
# functions 
def say_hi():
    print("Hello User")
say_hi()
def Say_Hi(name):
    print("Hello there " + name)
Say_Hi("Lulu Pinka")
def cube(num):
    result = num*num*num
    return result
print(cube(5))
age = 20
if age < 18:
    print("you are a minor")
elif age == 18:
    print("you are 18 years old")
else:
    print("you are old enough")
i = 0
while i <= 10:
    print(i)
    i += 1
for k in range(11):
    print(k)


