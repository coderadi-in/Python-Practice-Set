'''
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class JustAClass():
	def getString(self):
    	return input("Give a console input: ")

  	def printString(self, string: str):
    	print(string)

  	def test(self):
    	data = self.getString()
    	self.printString(data)

cls = JustAClass()
cls.test()
