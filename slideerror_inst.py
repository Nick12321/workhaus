class InvalidSlideError(Exception):
	def __init__(self, message):
		super().__init__()
		self.message = message