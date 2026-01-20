#printing a list of numbers through the user input 
n = int(input("Enter the length of the list: ")) # this will be the length of the list and it will be chosen by the user.
numbers = [] #this empty list will contain our list data that we input manually through the user input
i = 0
while i < n: # this loop helps us to iterate through our list as we manually input our list data
    new_number = int(input("Enter a number: ")) # we provide room for the users to input the list data
    numbers.append(new_number) # we append the numbers that are input by the users in the list
    i = i + 1
print(numbers)
# printing the elements of the list one by one 
i = 0
while i < n: #this loop allows us to iterate through the list 
    print(numbers[i])
    i = i +1
#finding the maximum value in a list 
max_value = numbers[0] #we first assume that the maximum value is the value at the start of the list
i = 0 
while i < n: # this loop helps us traverse through the list and we check for the maximum values 
    if numbers[i] > max_value:#this updates the maximum value if we get a value that is greater than the value we started with during the traversal.
        max_value = numbers[i] #update the max value if we get a bigger value.
    i = i + 1
print("The maximum value in the list is " + str(max_value)) #print the max value after all the traversal through the whole list.
# getting the position of the maximum value 
max_pos = 0 # we assume that the first value in the list is the maximum value in the list 
max_value = numbers[0]
i = 0 
while i < n: #this loop helps us traverse through the whole list while getting our comparisons 
    if numbers[i] > max_value: 
        max_value = numbers[i] #this updates the maximum value from the start position if we get any number that is greater than it during the traversal
        max_pos = i # we also update the maximum position in this case 
    i = i + 1 # update 
print("The index with the maximum position is " + str(max_pos))
# finding the minimum value in a list 
min_value = numbers[0]# we assume that the number at the start of the list is the minimum value of the list 
i = 0 
while i < n:
    if numbers[i] < min_value: 
        min_value = numbers[i]# this updates the minimum value if we get other minimum values in the list during the traversal
    i = i + 1 
print("The minimum value in the list is " + str(min_value))
# finding the minimum value index 
min_pos = 0 # we assume that the minimum value is at the start of the list 
min_value = numbers[0]
i = 0
while i < n:
    if numbers[i] < min_value: #this updates both the minimum position and value if we get any other minimum values in the list 
        min_value = numbers[i]
        min_pos = i 
    i = i + 1
print("The index with the minimum value is " + str(min_pos))
# counting the number of even numbers in the created list by the user
j = 0 # this will aid in the traversing through the list while looking for the even numbers
count = 0 # this aids while counting the even numbers 
while j < n: # traversal through the list 
    if numbers[j] % 2 == 0:
        count = count + 1 # if the remainder when the elements are divided by 2 is zero then count variable is increamented.
    j = j+ 1
print("There are " + str(count) + " even numbers in the list.")
# counting odd numbers in the list created 
j = 0 
count = 0 # count variable that helps us count the odd numbers in the list
while j < n:
    if numbers[j] % 2 != 0: # for odd numbers they are not divisible by 2 
        count = count + 1 # increament count when we find an odd number in the list 
    j =j + 1
print("There are " + str(count) + " odd numbers in the list.")
#getting numbers that are greater than 10 in the list 
j = 0
count = 0 # variable that aids us in the counting of the elements 
while j < n:
    if numbers[j] > 10: #looking for elements greater than 10
        count = count + 1 #increament count if you get an element that is greater than 10
    j = j + 1
print(str(count) + " numbers from the list are greater than ten.")
# how many two digit numbers are there in the list 
j = 0 
count = 0 # counting variable that enables us to count the double digit elements in the list while traversing.
while j < n:
    if numbers[j] >= 10 and numbers[j] <= 99: #the double digit numbers are between 0 and 99.
        count = count + 1 # increament the count variable if you find any double digit number in the list 
    j = j + 1
print("There are " + str(count) + " double digit numbers in the list.")
# counting the single double and triple digit elements in the list and also elements that have more than three digits in the list 
k = 0 # this variable will also help me traverse through the array 
count_1 = 0 # this helps us count the single digit numbers 
count_2 = 0 # this variable helps us count the double digit numbers 
count_3 = 0 # this helps us count the triple digit numbers 
count_4 = 0 # this helps us count the ones that have more than three digits 
while k < n: # traversing through the list
    if numbers[k] >=0 and numbers[k] <= 9: #single digit numbers are between 0 and 9
        count_1 = count_1 + 1 # increament the counting variable 
    elif numbers[k] >= 10 and numbers[k] <= 99: #double digit numbers are between 10 and 99
        count_2 = count_2 + 1 #increament the counting variable
    elif numbers[k] >= 100 and numbers[k] <=999: # triple digit numbers are between 100 and 999
        count_3 = count_3 + 1 #increament the counting variable 
    elif numbers[k] >= 1000: # for numbers with more than three digits 
        count_4 = count_4 + 1 # increamenting the counting variable 
    k = k + 1
print("There are " + str(count_1) + " single digit numbers in the list.")
print("There are " + str(count_2) + " double digit numbers in the list.")
print("There are " + str(count_3) + " triple digit numbers in the list.")
print("There are " + str(count_4) + " numbers with more than three digits in the list.")
#check if atleast one element of a list matches a given condition 
# you need a function that describes the wholr match function and also different functions for the different conditions 
def one_match(arr, condition):
    i = 0 
    found = False
    while i < n and found == False:
        if condition(arr[i]):
            found = True 
        i = i +1
    return found 
def Check_for_even(g):
    return g % 2 == 0
def value_greater_than_5(h):
    return h > 5 
print(one_match(numbers, Check_for_even))
print(one_match(numbers, value_greater_than_5))

#checking if all the elements in a list meet a certain condition 
def all_match(arr, condition):
    i = 0
    all_matches = True #this boolean data type will help us keep track of the numbers that match the condition and those that don't match the condition.
    while i < n and all_matches == True:
        if not condition(arr[i]): #this code runs if the element we traverse to in the list does not meet the condition in the function
            all_matches = False # we assign all_matches boolean to False 
        i = i + 1
    return all_matches 
def value_greater_than_5(m): # this is the condition function
    return m > 5 
print(all_match(numbers, value_greater_than_5))




 


