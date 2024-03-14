def binary_search(arr, target):
    """
    Performs binary search on a sorted list to find the index of the target element.
    
    Parameters:
        arr (list): A sorted list of elements.
        target: The element to search for in the list.
        
    Returns:
        int: The index of the target element if found, or -1 if not found.
        
    Important note:
        Performing binary search we have to assume that the we have to assume 
        that the array must be sorted while performing binary search
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1

        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # If target is not present in array
    return -1

# Example usage:
arr=[]
size=int(input("Enter how many numbers you want to insert in the array: "))
for element in range(size):
    ele=int(input("Enter the element at index {}: ".format(element)))
    arr.append(ele)
print("The array is now:", arr)
target=int(input("Enter the target element to find in the array: "))
result = binary_search(arr, target)

if result != -1:
    print("Element", target, "is present at index", result)
else:
    print("Element", target, "is not present in the array")
