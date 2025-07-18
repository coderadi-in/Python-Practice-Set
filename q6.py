'''
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
'''

import math

# print(math.floor(math.sqrt((2 * 50 * 100)/30)))

nums = input("Enter comma separated digits: ")
nums = nums.split(',')
nums = [int(num) for num in nums]

def calculate(nums: list):
  res = []
  C, H = 50, 30
  for D in nums:
    res.append(str(
      math.floor(math.sqrt((2 * C * D)/H))
    ))

  return ",".join(res)

print(calculate(nums))
