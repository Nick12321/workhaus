class MyCustomError(Exception):

	def __init__(self, message):
		super().__init__()
		self.message = message

class MyAwsomeClass:

	def testRaisingException(self):
		raise MyCustomError("Some error happened")


myAwesomeClass = MyAwsomeClass()
myAwesomeClass.testRaisingException()
