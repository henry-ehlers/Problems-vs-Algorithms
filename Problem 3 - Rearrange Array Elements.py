def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    if not isinstance(input_list, list):
        return [None]

    if len(input_list) == 0:
        return [None]

    if len(input_list) == 1:
        return [input_list[0]]

    # Merge Sort
    sorted_list = merge_sort(input_list)

    # initialize two empty lists: one for the unjoined numbers, one for the joined ones
    unjoined_nums = [[], []]
    joined_nums = []

    # Step throug sorted vector and populate the two lists
    index = 0
    while index < len(sorted_list):
        for num in unjoined_nums:
            if index < len(sorted_list): 
                num.append(sorted_list[index])
                index += 1
    
    # Join the two numbers 
    for num in unjoined_nums:
        #print(int(''.join([str(int) for int in num])))
        joined_nums.append(int(''.join([str(int) for int in num])))
    
    # return
    return joined_nums


def merge_sort(in_list):

    # Ensure the provided list is actually a list
    if not isinstance(in_list, list):
        exit("Provided object not of Type list")

    # Ensure The input list is actually not empty
    if not (len(in_list) > 0) :
        return in_list

    # Define the initial split
    mid_point = len(in_list) // 2
    left_half = in_list[0:mid_point]
    rigt_half = in_list[mid_point:len(in_list)]

    # Recursively merge and sort
    return merge(left_half, rigt_half)

def merge(left_half, rigt_half):
    # print("\n--------")
    # print(left_half)
    # print(rigt_half)

    # Initialize empty vector
    merged = []

    # Catch incase something breaks
    if (len(left_half) == 0) or (len(rigt_half) == 0):
        exit("SOMETHING WENT WRONG SOMEWHERE.")

    # Recursively break list into smaller and smaller pieces until len = 1
    if (len(left_half) > 1):
        #print("Left Recursion")
        mid_point = len(left_half) // 2
        #print(mid_point)
        left_half = merge(left_half[0:mid_point], left_half[mid_point:len(rigt_half)])
    if (len(rigt_half) > 1):
        #print("Right Recursion")
        mid_point = len(rigt_half) // 2
        #print(mid_point)
        rigt_half = merge(rigt_half[0:mid_point], rigt_half[mid_point:len(rigt_half)])

    # Initialize indeces of the two halves
    rigt_index = 0
    left_index = 0

    # Merge Sort
    while (left_index < len(left_half)) and (rigt_index < len(rigt_half)):
        if left_half[left_index] > rigt_half[rigt_index]:
            merged.append(left_half[left_index])
            left_index += 1
        else:
            merged.append(rigt_half[rigt_index])
            rigt_index += 1

    # Technically only of these needs to exist, but this works
    merged += left_half[left_index:]
    merged += rigt_half[rigt_index:]
    
    # Return Merged and sorted list
    return merged


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if output[0] != None:
        if sum(output) == sum(solution):
            print("Pass")
        else:
            print("Fail")
    else:
        if output[0] == solution[0]:
            print("Pass")
        else:
            print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[], [None]])
test_function([[7], [7]])

