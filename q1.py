'''
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

st = 2000
end = 3200
d = 7
m = 5

def filter_num(
	st: int=2000,
	end: int=3200,
	d: int=7,
	m: int=5
):
	nums = []
  	for i in range(st, end+1):
    	if (i % 7 == 0) and (i % 5 != 0):
        	nums.append(str(i))

  	return ", ".join(nums)

print(filter_num())
