def sort_012(in_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    # Ensure the input is indeed of type "list"
    if not isinstance(in_list, list):
        exit("Intput not of type list.")

    # Ensure the input list is at least of vector of length 1
    if len(in_list) < 1:
        return in_list

    # Ensure the input vector is numeric
    if not all(isinstance(element, int) or isinstance(element, float) for element in in_list):
        exit("Unexpected Value in input list.")

    # Initialize empty vector of legth of input vector
    out_list = [None] * len(in_list)

    # Initialize counters for 0's, 1's, and 2's
    zros = 0
    ones = 0
    twos = 0
    
    # Count the numbers of 0's, 1's, and 2's
    for value in in_list:
        if value == 0:
            zros += 1
        elif value == 1:
            ones += 1
        elif value == 2:
            twos += 1

    # Fill intialized vector with 0's, 1's, and 2's
    out_list[0:zros] = [0] * zros
    out_list[zros:(zros+ones)] = [1] * ones
    out_list[(zros+ones):(zros+ones+twos)] = [2] * twos

    # Return Soted output vector
    return out_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 0, 0, 0, 0, 0])
test_function([1, 1, 1, 1, 1])
test_function([2, 2, 2, 2])
test_function([])
test_function(["a", "a", "b", "b", "c", "a"])
test_function(5)