'''
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''

# text = input("Enter comma separated words: ")
# print(",".join(sorted(text.split(","))))

print(  ",".join(sorted(input("Enter comma separated words: ").split(","))))
