# Method name:
# find_kth_from_end

#Find the item that is a certain number of steps away from the end of the linked list WITHOUT USING LENGTH.
# For example, let's say you want to find the item that is 3 steps away from the end of the LL. 
# To do this, you would start from the head of the LL and move through the links until you reach the item that is 3 steps away from the end.
# This is the problem of finding the "kth node from the end" of a linked list. 
#Your task is to write a program that takes as input a linked list and a number k, and returns the item that is k steps away from the end of the list. 
# If the linked list has fewer than k items, the program should return None.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  
    # self solution
    def find_kth_from_end(self, k):
        # flip the linkedlist first
        # change the head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp
        # chang the mid
        previous = None
        current = self.head
        while current:
            current.next = previous
            previous = current
            current = current.next
        # start to find the kth item
        fd = self.head
        for _ in range(k):
            fd = fd.next
        return fd
    
    # course solution(use 2 pointer, a little bit like find middle node)
    def find_kth_from_end(ll, k):
        # Initialize both slow and fast pointers to 
        # # the head node of the linked list
        slow = fast = ll.head  

        # Move the fast pointer k nodes ahead of the slow pointer
        # If fast pointer reaches the end (None) before k nodes, 
        # the linked list is too short and kth node doesn't exist
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next
 
        # Move both pointers one node at a time until the fast 
        # pointer reaches the end of the linked list (None).
        # The slow pointer will now be pointing at the kth node 
        # from the end of the linked list.
        while fast:
            slow = slow.next
            fast = fast.next
        
        # Return the kth node from the end of the linked list
        return slow
    