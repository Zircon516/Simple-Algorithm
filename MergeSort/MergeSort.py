# Merge Sort
# break the item untile we get n list,
# n is the number of item in original list
# then combine each 2

# merge: helper function
# useful when 2 lists are both sorted
def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
             combined.append(list1[i])
             i += 1
        else:
            combined.append(list2[j])
            j += 1
    
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


# merge sort(need use recursion)
def merge_sort(my_list):
    # base case: when len(the_list) is 1
    if len(my_list) == 1:
        return my_list
# breaks lists in half
    mid_index = int(len(my_list)/2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)

# use merge() to put lists together


