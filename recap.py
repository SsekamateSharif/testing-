from math import*
character_name = "John"
character_age = "31"
character_home = "Cluj-Napoca"
print("My name is " + character_name + " I am " + character_age + " years old and I live in " + character_home + " Romania in Eastern Europe.")
#working with strings 
#escape sequences 
print("Elephant\nAcademy")
print("Elephant\"Academy") 
#appending 
phrase = "Giraffe Academy"
print(phrase + " zoo.")
#string functions
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("A"))
print(phrase.replace("Giraffe", "Lion"))
#working with numbers; both positive and negative numbers and also decimals
#maths functions that don't need importing files 
x = -10
print(abs(x))
print(pow(10,2))
print(5%2)
print(max(10,5))
print(min(10,5))
print(round(1.555))
#these require importing files
print(floor(1.555))
print(ceil(1.55))
print(sqrt(64))
#lists
my_list = [1,2,3,4]
print(my_list)
friends = ["Joan", "Lee", "Tonny"]
print(friends)
print(friends[1:])
print(friends[1:2])
#lists functions 
friends.append("lisa")
print(friends)
friends.extend(my_list)
print(friends)
friends = ["Joan", "Lee", "Tonny"]
print(friends)
friends.insert(1, "Lisa")
print(friends)
friends[3] = "Hakim"
print(friends)
friends.remove("Lee")
print(friends)
print(friends.index("Hakim"))
friends.insert(0, "Hakim")
print(friends)
x = friends.count("Hakim")
print(x)
my_list.reverse()
print(my_list)
my_list2 = my_list.copy()
print(my_list2)
my_list2.sort()
print(my_list2)
#Tuples; Are more like lists but their contents are constant and they cannot ne modified at any time 
my_tuple = (1,2,3,4,5)
print(my_tuple)
#Functions in python
#function that says happy birthday to the user three times 
def happy_birthday(name):
    print("happy birthday " + name)
    print("happy birthday " + name)
    print("happy birthday " + name)
happy_birthday("Iksan")
#functions to calculate area of a rectangle, square and circle, also perimeter of a square and rectangle and also circumference of a circle
def area_of_square_rectangle(length, width):
    result = length * width
    return result
x = area_of_square_rectangle(5,4)
print(x)
def circle_area(radius):
    result = pi * (radius * radius)
    return result 
x = circle_area(7)
print(x)
def perimeter (length, width):
    result = 2 * (length + width)
    return result 
x = perimeter(5,4)
print(x)
def circumference(radius):
    result = 2 * pi * radius
    return result
x = circumference(7)
print(x)
#if statements 
age = 22
if age == 21:
    print("You are 21 years old bro.") 
elif age == 22:
    print("You are older or younger than 21 years old bro.")
else:
    print("You are not 21 years old bro")
is_male = False
is_tall = False
if is_tall and is_male:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are a tall female")
else:
    print("you are a short female")
#user input; its got in string form therefore if you want to use them as numbers you have to do a type conversion 
name = input("Enter your name: ")
print("How are you doing " + name)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = num1 + num2 
print(num3)
#loops; for increaments and decreaments using the while loop
num4 = 0
i = num4 
while i <= 10:
    print(i)
    i = i +1
num5 = 10 
i = num5 
while i >= 0:
    print(i)
    i = i - 1
# for loops are used to traverse through list's content 
var_list = [34,35,45,56,67,32]
n = len(var_list)
for index in range(n):
    print(var_list[index])
#trying decrement and increment using the for loop
i = 0 
for i in range(10):
    print(i)
i = 10
#fizzbuzz game using the while loop
num6 = 1
k = num6 
while k <= 100:
    if k%3 == 0 and k%5 ==0:
        print(str(k) + " ->FizzBuzz")
    elif k%3 == 0 and k%5 !=0:
        print(str(k) + " ->Fizz")
    elif k%3 != 0 and k%5 == 0:
        print(str(k) + " ->Buzz")
    else:
        print(str(k))
    k = k + 1

