def swap(a, b, arr):
    '''
    Function to swap elements at indices a and b in the array arr.
    '''
    if a != b:  # If the indices are different
        tmp = arr[a]  # Store the value at index a temporarily
        arr[a] = arr[b]  # Assign the value at index b to index a
        arr[b] = tmp  # Assign the temporary value to index b


def partition(elements):
    '''
    Function to partition the elements around a pivot.
    '''
    pivot_index = 0  # Index of the pivot element
    pivot = elements[pivot_index]  # Pivot element
    start = pivot_index + 1  # Starting index for comparison
    end = len(elements) - 1  # Ending index for comparison
    while start < end:  # Loop until start and end indices meet

        # Move the start index to the right until we find an element greater than pivot
        while elements[start] <= pivot:
            start += 1

        # Move the end index to the left until we find an element less than or equal to pivot
        while elements[end] > pivot:
            end = end - 1

        # If start index is still less than end index, swap elements at start and end indices
        if start < end:
            swap(start, end, elements)

    # Swap pivot element with element at end index
    swap(pivot_index, end, elements)




             