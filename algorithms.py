from math import* 
# in this file i am going to be practicing all the algorithms that I have learnt 
# linear search: this works for unsorted lists and every element in the list is checked up hence it has a time complexity of O(n).
def linear_search(key,arr):
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] == key:
            return i
        i = i + 1
    return "Not Found" # if the element is not found it should return the words not found.
#Binary search: this works on only sorted lists in ascending order and it follows divide and conquer strategy whereby it divides the list into two parts.
def binary_search(key,arr):
    l = 0
    r = len(arr)-1
    while l <= r:
        mid = ((l+r)//2)
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
          r = mid - 1
        else:
          l = mid + 1
    return "Not found"
#bubble sort: sorting where by you have traversals that involve a set of comparisons and each traversal or pass puts one element in its position
# we need two loops; one loop that iterates through the traversals that put the elements in their positions and the loop for the comparisons of the elements
def bubble_sort(arr):
    n = len(arr)
    i = 0
    while i < n:
        j = 0
        while j < n -1 - i:
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            j = j + 1 
        i = i + 1 
    return arr 
#insertion sort; sorting Algorithm that follows the divide and conqure strategy where by the list is divided into the sorted subunit and unsorted subunit 
#we solve the sorted subunit into the unsorted subunit. The loop for traversing through the unsorted subunit has to be increamenting.
# the loop for traversing through the sorted subnit and doing all those comparisons has to be decreamenting.
def insertion_sort(arr):
    n = len(arr)
    i = 1 
    while i < n:
        temp = arr[i]
        j = i - 1
        while arr[j] > temp and j>=0:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = temp
             
        i = i + 1
    return arr

     
my_list = [1,23,44,55,12]
x = bubble_sort(my_list)
print(x)
g = insertion_sort(my_list)
print(g)
x = linear_search(44, my_list)
print(x)
x = linear_search(12, my_list)
print(x)
# lets put another scenario if we are searching for an element that is not in the list
x = linear_search(77, my_list)
print(x)
your_list = [1,3,5,7,9,11,13,15,17]
y = binary_search(13, your_list)
print(y)
y = binary_search(21, your_list)
print(y)
aab = [12,23,45,6767,8,77,85,32,22,33,1]
print(insertion_sort(aab))