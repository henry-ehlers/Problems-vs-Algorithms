def get_min_max(integers):
	"""
	Return a tuple(min, max) out of list of unsorted integers.

	Args:
		ints(list): list of integers containing one or more integers
	"""
	if not isinstance(integers, list):
		exit("Intput not of type list.")

	# Check if input is at least of length 1
	if not len(integers) > 0:
		return [None, None] 

	# Ensure the input vector is numeric
    if not all(isinstance(element, int) or isinstance(element, float) for element in in_list):
        exit("Unexpected non-integer or float value type in input list.")

	# Initialize largest and smallest values
	smallest = float("inf")
	largest  = float("-inf")

	# Iterate over all values in integer array
	for integer in integers:

		# If current integer is smaller than recorded smallest -> replace
		if integer > largest:
			largest = integer

		# If current integer is larger than recorded largest -> replace
		if integer < smallest:
			smallest = integer

	# Return
	return [smallest, largest]

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print(get_min_max([])) # returns None
print(get_min_max(["a", "a", "b", "b", "a", "c"])) # non-0 exit (not numeric)
print(get_min_max(l)) # non-0 exit (not list)
