from slide import Slide
from slideerror import InvalidSlideError

class SlideShow:

	def __init__(self):
		self.start = None
		self.end = None
		self.current = None

	def add(self, slide):
		if not isinstance(slide, Slide):
			message = "Invalid Slide given: " + str(slide)
			raise InvalidSlideError(message)
		if self.start == None:
			self.start = slide
			self.end = slide
			self.current = slide
			return
		slide.previous = self.end
		self.end.next = slide
		self.end = slide

	def printCurrentSlide(self):
		print(self.current)

	def goToNextSlide(self):
		if self.current.next:
			self.current = self.current.next

	def goToPreviousSlide(self):
		if self.current.previous:
			self.current = self.current.previous

	def __str__(self):
		currentSlide = self.start
		slideString = ""
		while currentSlide:
			slideString = slideString + currentSlide.__str__() + "\n"
			currentSlide = currentSlide.next
		return slideString


if __name__ == "__main__":
	slideShow = SlideShow()
	slide1 = Slide(1, "My Awesome Presentation", "Awesome stuff!")
	slide2 = Slide(2, "Technology", "Awesome tech stuff!")
	slide3 = Slide(3, "User Experince", "Awesome UX stuff!")
	slideShow.add(slide1)
	slideShow.add(slide2)
	slideShow.add(slide3)

	print("Test all slides...")
	print(slideShow)

	print("Test navigation...")
	slideShow.goToNextSlide()
	slideShow.printCurrentSlide()
	slideShow.goToPreviousSlide()
	slideShow.goToPreviousSlide() #should change nothing
	slideShow.goToPreviousSlide() #should change nothing
	slideShow.printCurrentSlide()

	print("\nTest InvalidSlideError")
	try:
		slideShow.add(None)
	except InvalidSlideError as e:
		print("InvalidSlideError: " + e.message)
