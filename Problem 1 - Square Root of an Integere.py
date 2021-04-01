def sqrt(input_number) :
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    # Ensure the Input is actually numeric
    # Source: https://stackabuse.com/python-check-if-variable-is-a-number/
    if not ((type(input_number) == int) or (type(input_number) == float)):
    	return None

    # Ensure Number is larger than 0 (if not, then there can be no valid sqrt)
    if input_number < 0 :
    	return None

    # Avoid recursion if input is zero, because midpoint cannot be calculated
    if (int(input_number) == 0) :
    	return 0

    # Return 1 if input is 1, because midpoint cannot be calculated
    if (int(input_number) == 1):
    	return 1

    # Find square root using divide and conquer
    # Discussed in lesson #3, with example of finding kth larger number
    # Similar solution discussed on forum here:
    # https://practice.geeksforgeeks.org/problems/how-to-find-square-root-of-a-large-number-in-ologn-time
    runner_low = 0
    runner_hig = int(input_number)
    runner_mid = runner_low + (runner_hig - runner_low) // 2
    return sqrt_rucursion(runner_low, runner_mid, runner_hig, input_number)

def sqrt_rucursion(runner_low, runner_mid, runner_hig, target) :

	# Calculate current estimates of the square
	current_square = runner_mid * runner_mid

	# Figure out which half of possibility space to investigate
	if current_square == target : return runner_mid
	# If current estimate of square to large, then search lower half
	elif current_square > target: runner_hig = runner_mid
	# If current estimate of square to high, search upper half
	else: runner_low = runner_mid

	# If midpoint can exist, calculate it and recurse
	if runner_hig > (runner_low + 1) :
		runner_mid = runner_low + (runner_hig - runner_low) // 2
		return sqrt_rucursion(runner_low, runner_mid, runner_hig, target)
	# If it does not, use low runner as floor estimate of sqrt
	else:
		return runner_low


# Test Case #1 - Ensure Negative Number does not break
print ("On -9: \t" + ("Pass" if (None == sqrt(-9)) else "Fail"))

# Test Case #2 - Ensure string does not break
print ("On '9': " + ("Pass" if (None == sqrt("9")) else "Fail"))

# Test case #3 - Ensure passing of float instead of integer works
print ("On 9.4: " + ("Pass" if (3 == sqrt(9.4)) else "Fail"))

# TEst Case #4 - Ensure Finding possible unevern int sqrt works
print ("On 9: \t" + ("Pass" if (3 == sqrt(9)) else "Fail"))

# Test case #5 - Ensure 0 doesn't break everything
print ("On 0: \t" + ("Pass" if (0 == sqrt(0)) else "Fail"))

# Test case #6 - Ensure 1 doesn't break everything
print ("On 1: \t" + ("Pass" if (1 == sqrt(1)) else "Fail"))

# TEst Case #7 - Ensure Finding possible even int sqrt works
print ("On 16: \t" + ("Pass" if (4 == sqrt(16)) else "Fail"))

# Test Case #8 - Ensure floor int estimate works
print ("On 27: \t" + ("Pass" if (5 == sqrt(27)) else "Fail"))
