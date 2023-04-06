class Node: # create new node
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value) -> None: # initilize new linedlist
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self): # print that linked list
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value): # create new node and add it to the end
        new_node = Node(value)
        if self.head is None: # if empty linked list, let the new node initialize
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1 
        return True # this funcation will be call again, so we need a return

    def pop(self):
        if self.head is None: # situation 1: an empty linkedlist
            return None
       # situation 2: have one or more elements
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        if self.length == 0: 
            # for the situation that linkedlist have only one element
            # only one element will not lead empty linkedlist if use the loop above, it only will decrease length
            self.head = None
            self.tail = None
        return temp # return the temp we just remove


    def prepend(self,value): # create new node and add it to the beginning
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True
    
    def popFirst(self): # pop the first item in the linkedlist
        if self.length == 0:
            return None
        temp = self.head # create this because we need a return op poped
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index): # return the node that in specific index
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index): 
            temp = temp.next
        return temp.value
    
    def set_value(self, index, value): # set a value in specific position of node
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value

        # also we can use get() method to directly get that node
        temp = self.get(index)
        if temp: # test if get a none 
            temp.value = value
            return True
        return False # if get a none, return false
    
    def insert(self, index, value): # insert a node in specific position
        if index < 0 or index >= self.length:
            return False
        temp = self.head
        pre = self.head
        for _ in range(index):
            pre = temp
            temp = temp.next
        new_node = Node(value)
        pre.next = new_node
        new_node.next = temp
        self.length += 1
        return True

        # use method directly
        if index < 0 or index >= self.length: # for out of range
            return False
        if index == 0: # for in the beginning
            return self.prepend(value)
        if index == self.length: # for in the end
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index): # remove particular node in position
        if index < 0 or index >= self.length: # for out of range
            return None # return None instead of False, because 
            # if we successful insert node, we return true, fail return false
            # when pop, if successful return node, if fail, return the opposite of node, none
        if index == 0:
            return self.popFirst(self)
        if index == self.length:
            return self.pop(self)
        prev = self.get(index - 1)
        temp = prev.next # why do not use temp = self.get(index), because it time is O(n), and directly next is O91)
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self): # switch tail and head, and all element back force
        # swhicth head and tail
        temp = self.head
        self.head = self.tail
        self.tail = temp
        # start to reverse
        after = temp.next
        before = None
        for _ in range(self.length): # understant this concept with graph
            after = temp.next
            temp.next = before
            before = temp
            temp = after

