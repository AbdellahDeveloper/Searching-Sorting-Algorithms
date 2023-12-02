def Binary_Search_Algorithm(list,value):
    list.sort()
    first_index = 0
    last_index = len(list) - 1
    middle_index = 0
    while first_index <= last_index:
        middle_index = (first_index + last_index)//2
        # If value is greater, ignore left half element
        if list[middle_index] < value:
            first_index = middle_index + 1
        # If value is smaller, ignore right half elements
        elif list[middle_index] > value:
            last_index = middle_index - 1
        # means x is present at mid
        else:
            return middle_index
    # The element isn't exist
    return -1