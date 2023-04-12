# stack
# last in, first out

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.hight = 1
    
    # print the stack
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    # add one node at top of the stack
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    
    # pop the node of top
    def pop(self):
        if self.heigh == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    
    
    
