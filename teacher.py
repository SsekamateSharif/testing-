# algorithm for calculating the average of three numbers 
num1 = 3
num2 = 55
num3 = 41
average = (num1 + num2 + num3)// 3
print(average)
# algorithm to calculate the average of three numbers from user input 
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")
average_number = (int(num1) + int(num2) + int(num3))// 3
print(average_number)
# determining if a number that is input by a user is an odd number 
number = int(input("Enter a number: "))
if number %2 != 0:
    print("The number is odd")
else:
    print("The number is not odd its even")
# getting the maximum number from three numbers 
num1 = 2
num2 = 4
num3 = 5
if num1 > num2 and num1 > num3:
    print(f"Maximum number: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"Maximum number: {num2}")
else:
    print(f"Maximum number: {num3}")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
if num1 > num2 and num1 > num3:
    print(f"Maximum number: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"Maximum number: {num2}")
else:
    print(f"Maximum number: {num3}")
#iterating through a list and printing its elements one by one. the list is  made from user input 
n = int(input("Enter the length of the array: ")) # allow the users to input the length of the array they want to make.
numbers = [] # form an empty array for storing the input data by the users
i = 0 
while i < n:
    new_number = int(input("Enter a number: "))
    numbers.append(new_number)
    i = i + 1
print( numbers)
# algorithm for finding the max value and max position from a list
def find_max(array):
    max_value = array[0] # we assume it to be the starting value in the list
    max_pos = 0 # we assume it to be the first position index of the list 
    i = 0
    while i < len(array):
        if array[i] > max_value: # updates the max_value if we find a value that is greater than it in the list 
            max_value = array[i]
            max_pos = i
            i = i + 1
        else: # if the value is lesser we keep the max_value as it is but we just move to another element in the list 
            i = i + 1
    return f"The maximum number is {max_value}  and the maximum position is {max_pos}"
numbers = [1,17,4,23,8]
print(find_max(numbers))
# counting even numbers in an array 
def count_even(array):
    count = 0 # this is our counting variable 
    i = 0 
    while i < len(array):
        if array[i] % 2 == 0:
            count = count + 1
            i = i + 1
        else:
            i = i + 1
    return count 
numbers = [1,17,4,23,8]
print(count_even(numbers)) 
# counting odd numbers 
def count_odd(array):
    count = 0
    i = 0 
    while i < len(array):
        if array[i] % 2 != 0:
            count = count + 1
            i = i + 1
        else:
            i = i + 1
    return count 
numbers = [1,17,4,23,8]
print(count_odd(numbers))
# linear search through an array 
def linear_search(array, key):
    i = 0 
    while i < len(array):
        if array[i] == key: # we get to an element that is equal to our key we return its position 
            return i 
        else:
            i = i + 1 # if its not equal to our key we move to the next index 
    return "element not found"
numbers = [1,17,4,23,8]
print(linear_search(numbers, 8))
print(linear_search(numbers, 34))
#binary search; only works for sorted arrays or lists 
def binary_search(array, key):
    l = 0
    n = len(array)
    r = n - 1
    while l <= r: #since when l > r element is absent
        mid = (l+r)//2
        if array[mid] == key:
            return mid 
        elif key > array[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return "element not found"
numbers = [1,2,3,4,5,6,7]
print(binary_search(numbers, 6))
print(binary_search(numbers, 18))
# checking if an element in a list meets a certain condition atleast one matches 
def atleast_one_match(arr, condition):
    i = 0 
    while i < len(arr):
        if condition(arr[i]): # this means if we traverse an element that matches the condition
            return True 
        else:
            i = i + 1 # if we traverse an element that does not meet the condition we just move to the next element 
    return False # if  we traverse through the whole list and we don't see any element matching the condition
def all_match(arr, condition): #function checks to see if all elements in a list match a certain condition if we get one that doesnot match we return false if we dont we return true.
    i = 0
    while i < len(arr):
        if not condition(arr[i]):
            return False 
        else:
            i = i + 1
    return True 
def even_no(n):
    return n % 2 == 0
numbers = [1,2,3,5,6,67]
print(atleast_one_match(numbers, even_no))
numbers = [1,3,5,7,9]
print(atleast_one_match(numbers, even_no))
numbers = [2,4,6,8,10]
print(all_match(numbers, even_no))
numbers = [2,4,6,8,13,10]
print(all_match(numbers, even_no))


