#linked lists; they are also a collection of data like arrays but their data is not stored in contigous memory units like arrays, its stored 
#in non-contigous units called nodes that store both data in that memory unit and also a pointer to the next node 
#Linked lists have two classes a class of the node and a class of the linked list methods 
class Node: #node class; this contains the data and the pointer to the next node 
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class linked_list: #linked list class that contains the methods of the linked list 
    def __init__(self, head= None): # this is afunction that defines the head node of the linked list 
        self.head = None
    def insert(self, data): # this is the function that aidss in the insertion of data into the newly formed head node 
        new_node = Node(data) #creating new nodes that initially point to none
        if self.head is None:
            self.head = new_node
            return 
        current_node = self.head # if head node has data in it 
        while current_node.next != None: # this loop runs until the next node is none this means until the last node since it points to none 
            current_node = current_node.next
        current_node.next = new_node
    def print(self): #this function helps to print the linked list 
        if self.head is None: # if the head node is empty then the linked list is empty 
            print("Invalid the head node is empty")
        else:
            current_node = self.head # our starting point is the head node 
            while current_node != None: # this loop loops as long as it iterates through a node that has data in it and it stops when it reaches a loop with out data in it.
                print(str(current_node.data) + "->")
                current_node = current_node.next # move to the next node 
            print("None")
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        current = self.head # if the head node has data, we have to traverse through the whole list until the last element
        while current.next != None: # checking if the next nodes to the head nodes are null while traversing through the linked list 
            current = current.next
        current.next = new_node #if the next node is null then the loop will stop and then it will have data inserted into it 
    def get_length(self):
        count = 0
        current = self.head
        while current != None: #this loop loops as long as the current nodes have data in them
            count += 1
            current = current.next
        print(count)
    def remove_At(self, index):
        if index < 0:
            print("invalid index")
        elif index == 0:
            self.head = self.head.next 
        else:
            count = 0
            current = self.head 
            while current != None:
                if count == index - 1:
                    current = current.next.next
                    break 
                count = count + 1
            current = current.next 
    def insert_At(self, data, index):
        if index < 0:
            print("Invalid")
            return 
        if index == 0:
            new_node = Node(data)
            self.head.next = new_node 
            return 
        count = 0
        current = self.head 
        while current != None:
            if count == index -1:
                new_node = Node(data)
                current.next = new_node 
                break 
            current = current.next 
            count = count + 1
# stacks; these are data structures that are like arrays but they are different in a way they follow the last in first out hypothesis they are treated like a pile of books the last book to be on the pile is the first to be removed 
stk = [] # for stacks we use dynamic arrays or lists for creating space in memory for storing our stacks 
stk.append(2) # for pushing data into our stack
stk.append(4)
stk.append(6)
stk.append(8)
print(stk)
# to remove the elements using the last in first out hypothesis
x = stk.pop()
print(x)
print(stk)
#Queues # these follow the FIFO; first in first out 
from collections import deque
queue = deque() # initialisation
queue.append(1) # pushing data into the queue 
queue.append(3)
queue.append(5)
queue.append(7)
queue.popleft()# to remove data following the FIFO hypothesis
print(queue)
#heaps; these are data structures that are in form of a tree with branches where by the data is arranged in ascending order
import heapq
data = [1,22,3,2,2,45,67,78,79,89,44,53,889]
heapq.heapify(data) # this code turns data into a heap data structure 
print(data)
heapq.heappush(data, 46)
print(data)
heapq.heappop(data)
print(data)
heapq.heappushpop(data, 56)
print(data)
#sets; these are like sets but they are unordered  and are unindexed 
utensils = {"spoon", "forks", "plates", "bowls", "potatoes", "bananas"}
print(utensils)
utensils.add("face towel")
print(utensils)
utensils.remove("bowls")
print(utensils)
food = {"potatoes", "bananas", "yams", "cucumber", "cocoa"}
print(utensils.union(food))
print(utensils.difference(food))
print(utensils.intersection(food))
                

        
    
      

               
       


               




ll = linked_list()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert_at_end(6)
ll.print()
ll.get_length()
ll.remove_At(3)
ll.insert_At(2,78)

