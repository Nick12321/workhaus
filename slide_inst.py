class Slide:

	def __init__(self, slideId, slideTitle, slideContent):
		self.slideId =  slideId
		self.slideTitle = slideTitle
		self.slideContent = slideContent
		self.next = None
		self.previous = None

	def __str__(self):
		return str(self.slideId) + " - " +\
				self.slideTitle + " - " +\
				self.slideContent
