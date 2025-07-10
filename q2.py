'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''

def calculate_facto(n: int):
	if n == 0 or n == 1:
		return 1
	else:
		return n * calculate_facto(n-1)

def get_factorial(nums: list|int=8):
	if isinstance(nums, int):
		return calculate_facto(nums)
	
	if isinstance(nums, list):
		res = []
		for num in nums:
  			res.append(calculate_facto(num))
		return res

print(get_factorial([5, 8]))
