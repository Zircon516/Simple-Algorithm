# You are given a singly linked list and two integers m and n. 
# Your task is to write a method reverse_between within the LinkedList class 
# that reverses the nodes of the linked list from index m to index n (inclusive) in one pass and in-place.

# Input
# The method reverse_between takes two integer inputs m and n.
# The method will only be passed valid indexes (you do not need to test whether the indexes are out of bounds)

# Output
# The method should modify the linked list in-place by reversing the nodes from index m to index n.
# If the linked list is empty or has only one node, the method should return None.

# Example
# Suppose the linked list is 1 -> 2 -> 3 -> 4 -> 5, and m = 2 and n = 4. 
# Then, the method should modify the linked list to 1 -> 2 -> 5 -> 4 -> 3 .

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
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

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
    
    # course solution(need to understand combined with graph)
    # A method to reverse a linked list from node m to node n inclusive.
    # If the linked list is empty, then return None.
    
    #  The reverse_between method in a LinkedList class takes two integer inputs m and n and reverses the linked list between the nodes located at positions m and n, inclusive.
    # If the linked list is empty, the method returns None.
    # The method first creates a dummy node with value 0 and sets its next attribute to the head of the linked list. 
    # Then, it sets prev to the dummy node and iterates prev m times.
    # At this point, prev points to the node that precedes the m-th node.

    # Next, the method sets current to the m-th node and iterates through the linked list n-m times.
    # In each iteration, the method swaps the next pointers of current and its next node, thereby reversing the order of the nodes between positions m and n.
    # The method uses a temporary variable temp to store the next node of current, which is needed to perform the swap.
    # Finally, the method updates the head of the linked list to the next node of the dummy node.

    def reverse_between(self, m, n):
    
        # If the linked list is empty, then return None.
        if not self.head:
            return None
 
        # create a dummy node and connect it to the head.
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
 
        # move prev to the node at position m.
        for i in range(m):
            prev = prev.next
 
        # set current to the next node of prev.
        current = prev.next
    
        # Reverse the linked list from position m to n.(n-m times operations)
        for i in range(n - m):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
 
        # update the head of the linked list with the next node of the dummy.
        self.head = dummy.next

