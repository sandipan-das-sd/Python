'''
METHOD =>1
'''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    '''
     Splitting the array into two halves using the divide method
     The first half is called left and the second list is called right
    means we are applying here the divide method
    '''
    mid = len(arr) // 2
    left = arr[:mid]  # First half (0 to mid-1)
    right = arr[mid:]  # Second half (mid to all)
    left = merge_sort(left) # apply merge sort here means again divide method will apply
    right = merge_sort(right)  # apply merge sort here means again divide method will apply
    return merge_two_sorted_lists(left, right) #concure method will apply for the two list

def merge_two_sorted_lists(a, b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    # Comparing elements from the two lists and putting them in the sorted list
    while i < len_a and j < len_b:
        '''
        In this while loop, the traversal will run for both lists.
        Suppose list 'a' has a length of 3 and list 'b' has a length of 5 or vice versa,
        then the loop will traverse up to a length of 3 for both 'a' and 'b';
        it will not run up to a length of 5.
        '''
        if a[i] <= b[j]:
            # If any element in 'a' is smaller than the element in 'b', then put that element in the sorted list
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    # Adding remaining elements from the first list
    while i < len_a:
        sorted_list.append(a[i])
        i += 1

    # Adding remaining elements from the second list
    while j < len_b:
        sorted_list.append(b[j])
        j += 1

    return sorted_list

if __name__ == '__main__':
    arr = [10, 8, 6, 25, 65, 4]
    print(merge_sort(arr))
