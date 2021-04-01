def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    # Ensure the list is actually a list
    if not isinstance(input_list, list) :
        return -1

    # Ensure the List is actually long enough
    if not (len(input_list) > 0) :
        return -1 

    # If list length 1 or 2, simply check the values and return index
    if len(input_list) <= 2:
        return naive_search(input_list, number)

    # print("\n====================")
    # print(input_list)
    # print("List Length: {}".format(len(input_list)))
    # print("Target:      {}".format(number))

    # 
    ind_low = 0
    ind_hig = len(input_list) - 1
    ind_mid = (ind_low + ind_hig) // 2
    return search_recursion(input_list, ind_low, ind_mid, ind_hig, number)


def search_recursion(in_list, ind_low, ind_mid, ind_hig, target) :

    # print("-----------")
    # print(in_list[ind_low:(ind_hig+1)])
    # print("{} - {}".format(ind_low, in_list[ind_low]))
    # print("{} - {}".format(ind_mid, in_list[ind_mid]))
    # print("{} - {}".format(ind_hig, in_list[ind_hig]))

    # Check if mid indexed value is the target, if so return
    if in_list[ind_mid] == target:
        return ind_mid
    
    # Check if low < mid < height values
    if (in_list[ind_low] < in_list[ind_mid]) and (in_list[ind_mid] < in_list[ind_hig]) :
        ind_hig = ind_mid

    # Check if low < mid AND mid > heigh
    elif (in_list[ind_low] < in_list[ind_mid]) and (in_list[ind_mid] > in_list[ind_hig]) :
        if (in_list[ind_low] <= target) and (target < in_list[ind_mid]):
            ind_hig = ind_mid
        else:
            ind_low = ind_mid

    # Check if low > mid AND mid < heigh
    elif (in_list[ind_low] > in_list[ind_mid]) and (in_list[ind_mid] < in_list[ind_hig]) :
        #print("Sort Int")
        if (in_list[ind_mid] < target) and (target <= in_list[ind_hig]):
            ind_low = ind_mid
        else:
            ind_hig = ind_mid

    # Catch (shouldn't be necessary since under the assumption of sorted vectors, the previous checks should catch everything)
    else:
        exit("SOMETHING IS HORRIBLY BROKEN!")

    # Calculate Mid Index IF possible
    if ind_hig > (ind_low + 1):
        ind_mid = ind_low + (ind_hig - ind_low) // 2
    # If list is only 2 long, simply search the remaining elements
    else:
        return naive_search(in_list[ind_low:ind_hig], target)

    # Recurse using new low, mid, and high indeces
    return search_recursion(in_list, ind_low, ind_mid, ind_hig, target)

# Linearly go through list and check if element is there
# If so, return index, else, return -1
def naive_search(input_list, number):
    for index, value in enumerate(input_list):
        if value == number:
            return index
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Test Cases
test_function([[], None])
test_function([[1, 5], 5])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])