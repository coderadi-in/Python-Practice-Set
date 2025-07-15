'''
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

st = 1000
end = 3000
res = []

for i in range(st, end+1):
  even = True
  for n in list(str(i)):
    if int(n) % 2 != 0:
      even = False
      pass

  if even:
    res.append(str(i))

print(",".join(res))
