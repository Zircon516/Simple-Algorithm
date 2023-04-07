#Q1: Write a method to find and return the middle node in the Linked List WITHOUT using the length attribute.
#Method name: find_middle_node

class Node:
    '''create new node'''
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    '''create linkedlist'''
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        '''append new node to linkedlist'''
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
# self solution
# cons: still using num as counter.
    def find_middle_node(self):
        '''find a middle node'''
        # if a empty linkedlist
        if self.head is None:
            return None
        if self.head == self.tail:
            return self.head
        # find the middle node index
        num = 0
        cnt = self.head
        while cnt.next:
            num += 1
        # two situation
        # situation one: odd number
        if num % 2 == 1:
            # get that node with index (num+1)/2
            temp_odd = self.head
            for _ in range((num + 1) // 2):
                temp_odd = temp_odd.next
            return temp_odd
        # situation two: even number
        else:
            temp_even = self.head
            for _ in range(num // 2):
                temp_even = temp_even.next
            return temp_even, temp_even.next

#course solution
# This method uses two pointers, slow and fast, and advances them at different speeds through the list. 
# The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. 
# By the time the fast pointer reaches the end of the list, the slow pointer will be at the middle node.
    def find_middle_node_sol(self): # 让两个pointer速度不一致，一个是另一个速度的两倍，当快的走完全程，慢的恰好走完1/2
        '''find a middle node'''
        # Initialize two pointers to the head of the list
        slow = self.head
        fast = self.head

        # Traverse the list with the fast pointer moving twice
        # as fast as the slow pointer
        while fast is not None and fast.next is not None:
            slow = slow.next  # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps

            # When the fast pointer reaches the end, the slow
            # pointer will be at the middle node
        return slow
