from math import*
#varaibles in python; you can name them by their names i.e the variable names that you assign to them 
n= 13
print(n)
character_name = "Terry"
character_age = "35"
character_home = "Bucharest, ROMANIA."
character_religion = "christian"
print("Hey my name is " + character_name + " and I am " + character_age + " years old right now.")
print("I am " + character_religion + " and i live in " + character_home)
#working with strings; appending a string 
phrase = "Hello"
print(phrase + " there Adam")
# string functions; converting to lower case or upper case 
zoo = "Giraffe Academy"
print(zoo.lower())
print(zoo.upper())
#checking if its lower case or upper case 
print(zoo.isupper())
print(zoo.islower())
print(zoo.lower().islower())
print(zoo.upper().isupper())
#printing by index and the index function
print(zoo[1])
print(zoo.index("A"))
#length of a string and also replacing xters 
print(len(zoo))
print(zoo.replace("Giraffe", "Elephant"))
#working with numbers; arithmetic operations and functions 
X = 1 + 5
print(X)
x = 5 - 3
print(x)
x = 12 / 3
print(x)
#functions 
x = -13
print(abs(x))
print(pow(2,3))
x = (5%2)
print(x)
print(max(10,4))
print(min(10,4))
print(round(1.556))
# functions that need some files imported 
print(floor(1.333))
print(ceil(1.3333))
print(sqrt(25))
#getting user input; here we use the input key word 
name = input("Please enter your name: ")
print("Hello " + name + " how are you doing.")
# type conversion from number to string 
age = 35
print("My name is Tonny and am " + str(age) + " years old.")
# building a simple calculator 
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
result = float(num1) + float(num2) #since the two are input as strings we have to convert them to numbers
print(result)
#lists; these are used as a collection of different data types they are like the arrays in c++
list = [1,2,3,4,5]
print(list)
print(list[3])
# list functions; adding two lists together
lucky_numbers = [9,8,7,6,5,4]
friends = ["Kim", "Jon", "Unn"]
friends.extend(lucky_numbers)
print(friends)
#appending a list
friends = ["Kim", "Jon", "Unn"]
print(friends)
friends.append("Katty")
print(friends)
# inserting items in a list
friends.insert(3, "John")
print(friends)
#removing elements from a list; to erase the whole list use friends.clear()
friends.remove("Katty")
print(friends)
print(friends.index("John"))
friends.append("Kim")
print(friends.count("Kim"))
lucky_numbers.reverse()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
lucky_numbers.sort()
print(lucky_numbers)
numbers = friends.copy()
print(numbers)
# tuples; are jus like lists but they are different since they are unchangeable
hallo = (1,2,3,4)
print(hallo) # its order and elements are constant and unchangable
#functions; if you have like six lines of code that you would like to implement in different positions of your programme you need to make 
#a function for them and call that function when you want to implement their effect
# simple function that says hi.
def say_hi(): #creating the function
    print("Hi")
say_hi() #calling the function
# a function that says happy birthday to the user;
def happy_birthday(name):
    print("Happy birthday " + name + ".")
    print("Age like fine wine " + name)
    print("Enjoy your day " + name)
happy_birthday("Sharif")
# functions that have return values have return statements 
#cube function
def cube(n):
    return n * n * n
x = cube(2)
print(x)
def area(length, width):
    result = length * width
    return result
print (area(5,4))
def circle_area(radius):
    Pi = 3.1416
    result = Pi * (pow(radius, 2))
    return result
print(circle_area(7))
#conditional statements; if satements; using boolean data types 
is_male = False
is_tall = False 
if is_male and is_tall:
    print("You're  a tall male individual")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are a short female")
else:
    print("You are neither male nor tall")
#while using conditional operators; let me try to create a guessing game
name = "Sharif"
age = 21
name_guess = input("Enter a name: ")
age_guess = input("Enter an age: ")
if name == name_guess and age == int(age_guess):
    print("You guessed both my age and name right")
elif name == name_guess and age != int(age_guess):
    print("You guessed my name right but failed my age")
elif name != name_guess and age == int(age_guess):
    print("You guessed my age right but failed to guess my name")
elif name != name_guess and age != int(age_guess):
    print("You failed to guess both my age and my name right")
#dictionaries; these allow us to store keys and values in pairs, they act like normal dictionaries.
months_of_the_year ={
   #key : #value; hence these dictionaries allow us to store both the keys and the values together 
  "Jan" : "January",
  "Feb": "February",
  "Mar": "March",
  "Apr": "April",
  "May" :"May",
  "Jun":"June",
  "Jul":"July",
  "Aug":"August",
  "Sep":"September",
  "Oct": "October",
  "Nov": "November",
  "Dec": "December",
  }
#Dictionaries allow us to store both keys and values in pairs 
print(months_of_the_year["Jan"])
# i can also use dictionaries to translate a language since it stores both keys and values in pairs 
translate_from_English_to_Luganda = {
    "How are you":"Oli Otya",
    "Good Morning":"Wasuzze otya",
    "I love you": "Nkwagala",
    "I want food": "Njagala mmele",
}
# just call the word among the keys stored in the dictionary 
print(translate_from_English_to_Luganda["How are you"])
print(translate_from_English_to_Luganda["I love you"])
# dictionaries are used to store both the keys and the values in pairs 
#loops; while loops; these allow us to iterate through a certain range of data types and the iterate as long as the condition is true and 
# stop iterating if the condition is false 
#increamenting
i = 1 # initialisation 
while i <=10: # the condition
    print(i) #code to the executed during the iterations
    i = i+1 # the update to be followed during the iterations 
print("You are done")
#decreamenting
i = 10 #initialisation
while i >=0: #condition
    print(i) #code to be executed 
    i = i-1 #update
print("you are done")
#building a guessing game using while loop
number = 35
guess = ""
while guess!= number:
    guess = int(input("Enter a number: "))
print("well done you have guessed the number right.")
#for loop also allows us to loop through lists and strings and also a range of numbers 
zoo = "Giraffe Academy"
for letter in zoo:
    print(letter)# here we are iterating through a string called zoo using the for loop
# lets iteratw through a list using the for loop
list_fruits = ["Apples", "oranges", "peach","pine apples"]
for fruit in list_fruits:
    print(fruit) # this for loop iterates through the list and prints the elements of the list
# we can also iterate through a range of numbers 
for ivy in range(10):
    print(ivy) 
for ivy in range(3,10):
    print(ivy)
# we can also iterate through the list in another way 
for index in range(len(list_fruits)):
    print(list_fruits[index])
numbers = [1,2,3,45,66,78,9]
# reading through this list it has 7 elements 
for i in range(7):
   print(numbers[i])
# exponent function; used to find the exponent of a number 
def exponent_function(base,exponent):
    result = 1
    for index in range(exponent):
        result = base * result 
    return result 
print(exponent_function(2,3))
#2D lists and nested loops 
Two_D_lists =[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(Two_D_lists[0][0])
for row in Two_D_lists:
   for col in row:
       print(col)
#try and except
try:
    number = int(input ("Enter a number: "))
    print(number)
except ValueError:
    print("invalid input")
i = 10 
while i >= 0:
    print(i)
    i = i -2



    




