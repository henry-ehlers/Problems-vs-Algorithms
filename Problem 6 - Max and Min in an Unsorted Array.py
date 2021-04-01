def get_min_max(integers):
	"""
	Return a tuple(min, max) out of list of unsorted integers.

	Args:
		ints(list): list of integers containing one or more integers
	"""
	if not isinstance(integers, list):
		exit("Intput not of type list.")

	if not len(integers) > 0:
		return [None, None] 

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

print(get_min_max(l))