'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
'''

binary = input("Enter comma separated binary digits: ")
binary_dict = {}
res = []

for n in binary.split(","):
  binary_dict[n] = int(n, 2)

for binary, decimal in binary_dict.items():
  if decimal % 5 == 0:
    res.append(binary)

print(",".join(res))
