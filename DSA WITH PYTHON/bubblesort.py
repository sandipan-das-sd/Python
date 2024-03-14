def bubble_sort(arr):
    """
    Sorts the given list using the Bubble Sort algorithm with built-in function for swapping.
    
    Parameters:
        arr (list): The list to be sorted.
        
    Returns:
        list: The sorted list.
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        
        # Last i elements are already in place, so we can skip them
        for j in range(n - i - 1):
            # Traverse the array from 0 to n-i-1
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no two elements were swapped in the inner loop, the array is already sorted
        if not swapped:
            break
    
    return arr

# Example usage:
my_list = []
size = int(input("Enter how many numbers you want to insert in the array: "))
for element in range(size):
    ele = int(input("Enter the element at index {}: ".format(element)))
    my_list.append(ele)
print("The array is now:", my_list)
sorted_list = bubble_sort(my_list)
print("Sorted list using Bubble Sort:", sorted_list)
