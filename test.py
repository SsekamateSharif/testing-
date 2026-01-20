from math import*
#variables 
character_name = "John"
character_home = "Wakiso"
character_age = "36"
print("My name is " + character_name + ", I am " + character_age + " years old and I live in " + character_home)
# data types 
#strings; creating a new line and also the quotations in strings 
print("giraffe\nAcademy")
print("giraffe\"Academy")
#string functions 
phrase = "Giraffe Academy"
print(phrase.lower())
print(phrase.upper())
print(phrase.lower().islower())
print(phrase.upper().isupper())
greet = "Hello"
print(greet + " there Aron") 
print(len(phrase))
print(phrase[1])
print(phrase.index("A"))
print(phrase.replace("Giraffe", "Elephant"))
#working with numbers; simple arithmetic operations 
x = 1 + 2 
y = 3*4
print(x)
print(y)
# maths functions 
#absolute function
n = -6 
print(abs(n))
print(pow(10,2))
print(5%2)
print(max(10,5))
print(min(10,5))
print(round(1.4556))
print(floor(1.555))
print(ceil(1.555))
print(sqrt(16))
#lists; these are collections of data types, they work as arrays in other programming languages 
list = [1,2,3,4]
print(list)
print(list[0])
print(list[1:])
print(list[1:2])
friends =["John", "karen","kitty"]
print(friends)
#adding two strings 
friends.extend(list)
print(friends)
friends = ["john", "karen", "kitty"]
friends.append("jonah")
print(friends)
friends.insert(2,"Kevin")
print(friends)
friends.remove("Kevin")
print(friends)
print(friends.index("john"))
friends1 = friends.copy()
print(friends1)
list.reverse()
print(list)
list.sort()
print(list)
#tuples; these are like lists but they are unchangable and uneditable
tuple = (1,2,3,5)
print(tuple)
#functions; creating and calling functions 
def happy_birthday(name):
    print("Happy birthday to you " + name)
happy_birthday("Derrick")
#return statement for functions that have a return value 
def area(length, width):
    result = length * width
    return result
print(area(5,2))
#if statements; making  a guessing game where the user guesses my name and age
name = "Sharif"
age = 21
name_guess = input("Enter a name: ")
age_guess = float(input("Enter an age: "))
if name ==name_guess and age == age_guess:
    print("You have guessed both my name and my age right.")
elif name == name_guess and age != age_guess:
    print("You guessed my name right but failed to guess my age.")
elif name != name_guess and age == age_guess:
    print("You guessed my age right but failed to guess my name.")
else:
    print("You failed to guess both my name and age.")
#loops; while loops; you can use them to show increments and decrements 
i = 0
while i<=10:
    print(i)
    i = i+1
#for loop is used to iterate through lists and also through strings 
list = [43,44,54,56,57]
for i in range(4):
    print(list[i])
phrase = "Giraffe Academy"
print(len(phrase))
for i in range(15):
    print(phrase[i])
for i in range(10):
    print(i)
