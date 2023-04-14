# hash table
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size #create a list with 7 items in it, all of those contain None
    
    # create a hash mathod
    def __hash(self,key):
        my_hash = 0
        for letter in key:
            # ord() get the ASCII numerical value for each letter
            # *23, prime number
            # % used as calculate remainder
            # len(7), if divide any number by 7, the remaider will be 0-6(the address space)
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key) # calculate the address where we store value
        # initilize an empty list in that address
        if self.data_map[index] == None:
            self.data_map[index] = []
        # add the key value pair in the list
        self.data_map[index].append([key,value])
    
    # accept a key, hash it and get the address(if in hash table), return value; 
    # if not in hash table, return None
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    # take all of keys of hashtable and put them in a list, return that list
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys




