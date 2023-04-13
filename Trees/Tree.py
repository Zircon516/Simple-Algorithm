# tree
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        # new_node = Node(value)
        # self.root = new_node

        # can also initialize the root as None
        self.root = None
    
    def insert(self,value):
        new_Node = Node()
        # if tree is None
        if self.root == None:
            self.root = new_Node
            return True
        # if we have a root already
        temp = self.root
        while True: # while true
            if new_Node.value == temp.value: #if equal value, cannot insert
                return False
            if new_Node.value < temp.value:
                if temp.left is None: # if the spot is empty, then insert
                    temp.left = new_Node
                    return True
                temp = temp.left # else go ahead
            else:
                if temp.right is None:
                    temp.right = new_Node
                    return True
                temp = temp.right
    
    def contains(self,value):
        # if self.root == None: # we do not need this code, because the while loop will help us to judge
            # return False
        temp = self.root
        while temp is not None:
            if temp.value > value:
                temp = temp.left
            elif temp.value < value:
                temp = temp.right
            else:
                return True
        return False

