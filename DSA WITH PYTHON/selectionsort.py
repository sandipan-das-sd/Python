def selection_sort(arr):
    """
    Sorts the given list using the Selection Sort algorithm.
    
    Parameters:
        arr (list): The list to be sorted.
        
    Returns:
        list: The sorted list.
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# Example usage:
my_list=[]
size=int(input("Enter how many numbers you want to insert in the array: "))
for element in range(size):
    ele=int(input("Enter the element at index {}: ".format(element)))
    my_list.append(ele)
print("The array is now:", my_list)
sorted_list = selection_sort(my_list)
print("Sorted list using selection sort:", sorted_list)
