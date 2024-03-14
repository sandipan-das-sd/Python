def insertion_sort(arr):
    """
    Sorts the given list using the insertion Sort algorithm.
    
    Parameters:
        arr (list): The list to be sorted.
        
    Returns:
        list: The sorted list.
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key into its correct position
        arr[j + 1] = key
    
    return arr

# Example usage:
my_list = []
size = int(input("Enter how many numbers you want to insert in the array: "))
for element in range(size):
    ele = int(input("Enter the element at index {}: ".format(element)))
    my_list.append(ele)
print("The array is now:", my_list)
sorted_list = insertion_sort(my_list)
print("Sorted list using insertion sort:", sorted_list)
