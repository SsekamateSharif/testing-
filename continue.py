import random 
#merging two sorted arrays or lists algorithm
def merge(arr1, arr2):
    i = 0 # traversing variable for the first sorted list 
    j = 0 # traversing vraiable for the second sorted list
    arr3 = [] # the empty list that we are going to use during the merging of the two sorted lists 
    n = len(arr1) # length of the first list
    m = len(arr2) # length of the second list 
    while i < n and j < m: # this loop is traversing through both the first and the second sorted arrays or lists 
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i]) # if the element in first array is less than the element in second array we append to our new list and move to the next index.
            i = i + 1 # if this condition is true we increament the index of the first array but not the second array 
        else:
            arr3.append(arr2[j]) # if element in second array is less we append it to our new array
            j = j + 1 #if this condition is true we only increament the index of the second array
    # after reaching the end of one of the lists we will exit the loop above but we may have some numbers remaining un added to the new list 
    # and to add these numbers to the new list we need to traverse each list checking if we have reached the end of those lists and add them to our new list 
    while i < n: # this loop traverses through the first array if we have not yet reached its end and we have some elements un added to the new list 
        arr3.append(arr1[i])
        i = i + 1
    while j < m: # if we have not reached the end of the second list this loop helps us add the unadded elements to our new list 
        arr3.append(arr2[j])
        j = j + 1
    return arr3 # we have to return the merged solution of the lists 
my_list = [1,3,5,7,9]
your_list = [2,4,6,11,12,13,14]
print(merge(my_list, your_list))
# algorithm that gets the longest subsequest of elements that fulfill a certain requirement in a list.
# we have to first create the conditions functions 
def odd_numbers(m):
    return m % 2 != 0
def even_numbers(o):
    return o % 2 == 0
def longest_subsequence(arr,condition):
    max_pos = 0 # this is the position of the longest subsequence. Initially at 0
    max_length = 0 # this the length of the longest subsequence. Also initially at 0
    start_pos = 0 # this is the current position of the most current subsequence 
    start_length = 0 # the current length of the current subsequence
    i = 0 # index traversing variable 
    n = len(arr)
    while i < n: #traversing through the list 
        if condition(arr[i]): # if the element meets the condition
            if start_length == 0: #if the current length of the subsquence is 0 then make the current position equal to the index variable
                start_pos = i
            start_length = start_length + 1 # if the condition is true then we increament the current subsequences' length 
        else: # if the condition is not met by the element:
            if start_length > max_length: # updating the maximum length and position 
                max_length = start_length 
                max_pos = start_pos
            # reseting the starting length and position to 0 for the new subsequence 
            start_length = 0
            start_pos = 0
        i = i + 1 # increament the indexing variable 
    return (max_length, max_pos)

numbers = [3,5,6,7,9,1,33,4,5,6,8,10,12,14,66,8,7,9,1,3,5,7,8,9,7,8]
print(longest_subsequence(numbers, odd_numbers))
print(longest_subsequence(numbers, even_numbers))
#algorithm for finding how many times a digit appears in a list of random numbers using a frequency list or array.
numbers = [] 
i = 0 
while i < 10000: # creating our list with 10000 random numbers between 0 and 100
    new_number = random.randint(0,100)
    numbers.append(new_number)
    i = i + 1
frequency_list = [0] * 101 # creating a frequency list with 100 elements all initialised to 0 
i = 0 
while i < len(numbers): # increamenting the count at each index of the frequency list depending on the elements found in numbers 
    frequency_list[numbers[i]] = frequency_list[numbers[i]] + 1
    i = i + 1 
total_numbers = 0 # finding the total numbers in frequency list counts 
i = 0 
while i < len(frequency_list):
    total_numbers = frequency_list[i] + total_numbers
    print(f"The number {i} appears {frequency_list[i]} times")
    i = i + 1
print(f"The total number of digits is {total_numbers}")
# counting with dictionaries 
def count(arr):
    d = {}
    for item in arr:
        if item in d: #if the item is already in the dictionary increase its positions count by one 
            d[item] += 1
        else: #if it is not in the dictionary then insert it there 
            d[item] = 1
    return d 
very_list = [1,2,3,4,5,6,1,1,1,2,2,3,5,6,7,8,9,9,9,10]
print(count(very_list))
text = "abcdef"
print(text[-3:])
def count(elements):
    element = str(elements)
    d = {}
    for item in element:
        if item in d:
            d[item] = d[item] + 1
        else:
            d[item] = 1
    return d
name = "dagsahgahhashabbkjabkskj"
print(count(name))
num = 13255477854889589900
print(count(num))
