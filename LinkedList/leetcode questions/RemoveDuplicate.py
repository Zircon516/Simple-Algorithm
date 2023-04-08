#You are given a singly linked list that contains integer values, where some of these values may be duplicated.
#Your task is to implement a method called remove_duplicates() within the LinkedList class that removes all duplicate values from the list.
#Your method should not create a new list, but rather modify the existing list in-place, preserving the relative order of the nodes.
#You can implement the remove_duplicates() method in two different ways:
#Using a Set - This approach will have a time complexity of O(n), where n is the number of nodes in the linked list. You are allowed to use the provided Set data structure in your implementation.
#Without using a Set - This approach will have a time complexity of O(n^2), where n is the number of nodes in the linked list. 
#You are not allowed to use any additional data structures for this implementation.

#Here is the method signature you need to implement:
#def remove_duplicates(self):

#Example:
#Input:
#LinkedList: 1 -> 2 -> 3 -> 1 -> 4 -> 2 -> 5
#Output:
#LinkedList: 1 -> 2 -> 3 -> 4 -> 5

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next          

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    # self-solution(wrong)
    def remove_duplicates(self):
        temp = self.head
        val_list = []
        while temp:
            if temp.next.value not in val_list:
                val_list.append(temp.next.value)
                tamp = temp.next
            else:
                pre = temp.next
                temp.next = pre.next
                pre.next = None
    
    # course solution

    # solution 1: O(n)
    # For the optimal solution you will want to use a Set (you can read more about Sets here):
    # I have also included an implementation that does not use a Set at the bottom of this explanation.
    # Either solution will work but the one with Sets is O(n) while the other is O(n^2) time complexity.

    def remove_duplicates(self):
            values = set() # create a set that used to store value
            previous = None # create a poiter point to the previous
            current = self.head
            while current:
                if current.value in values: # if have such value in set
                    previous.next = current.next # cut the link between prev and curr, link prev to the curr next
                    self.length -= 1 # decrease len
                else:
                    values.add(current.value) # if not have such value, add that value in set
                    previous = current # move previous to the position of current
                current = current.next # move current one step forward
    
    # In this implementation, the linked list is iterated over using a while loop, 
    # with the current variable starting at the head of the linked list and the previous variable starting at None.
    # If the current node's value is in the set of values, it's a duplicate, so the previous node's next attribute is set to the current node's next attribute. 
    # This effectively removes the duplicate node from the linked list. 
    # If the current node's value is not in the set, it's added to the set, and the previous variable is set to current.
    # Finally, the current variable is set to the current node's next attribute, and the iteration continues until current is None.
    
    # solution 2:O(n^2)
    # You can also do this without a Set but this will change the Big O from O(n) to O(n^2):
    # A Set is a data structure that we will learn more about later in the course.
    # Here is the solution without using a Set:
    
    # for every item in linked list, examine all the following item to check whether have same value
    def remove_duplicates(self):
        current = self.head
        while current: # while current is not None
            runner = current
            while runner.next: # while the following of the current is not None
                if runner.next.value == current.value: # if the next value equals to the current value
                    runner.next = runner.next.next # link that item to the next item
                    self.length -= 1
                else:
                    runner = runner.next
            current = current.next