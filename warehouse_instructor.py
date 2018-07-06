from datetime import datetime

AREA1 = "A1"
AREA2 = "A2"
AREA3 = "A3"
AREA4 = "A4"

class Robot:
	def __init__(self, id):
		self.id = id

class InspectorRobot(Robot):

	def __init__(self, id):
		super().__init__(id)

	def inspect(self, item):
		if item.expiryDate == None:
			return True
		elif item.expiryDate > datetime.now():
			return True
		else:
			return False

class DecisionRobot(Robot):

	def __init__(self, id):
		super().__init__(id)

	def determinItemLocation(self, item):
		if item.postalCode == 'X1Y' or item.postalCode == 'Y1Y':
			return AREA1
		elif item.postalCode == 'Y1X' or item.postalCode == 'X2A':
			return AREA2
		elif item.postalCode == 'Y2A' or item.postalCode == 'Z3Z':
			return AREA3
		else:
			return AREA4

class LabelRobot(Robot):

	def __init__(self, id, designatedArea):
		super().__init__(id)
		self.designatedArea = designatedArea

	def labelItem(self, item):
		item.setLabel(self.designatedArea)


class Item:

	def __init__(self, name, expiryDate, postalCode):
		self.name = name
		self.expiryDate = expiryDate
		self.postalCode = postalCode
		self.label = None

	def setLabel(self, label):
		self.label = label

	def __str__(self):
		return self.name + "," + str(self.expiryDate) + "," + \
				self.postalCode + "," + self.label

class RobotWirehouse:

	def __init__(self):
		self.inspectorRobot = InspectorRobot("RI-01")
		self.decisionRobot = DecisionRobot("RD-01")
		self.labelRobotA1 = LabelRobot("RL-01", AREA1)
		self.labelRobotA2 = LabelRobot("RL-02", AREA2)
		self.labelRobotA3 = LabelRobot("RL-03", AREA3)
		self.labelRobotA4 = LabelRobot("RL-04", AREA4)
		self.items = []

	def getLableRobotForLocation(self, location):
		if location == AREA1:
			return self.labelRobotA1
		elif location == AREA2:
			return self.labelRobotA2
		elif location == AREA3:
			return self.labelRobotA3
		else:
			return self.labelRobotA4

	def addItem(self, item):
		if self.inspectorRobot.inspect(item) == True:
			self.items.append(item)
			location = self.decisionRobot.determinItemLocation(item)
			labelRobot = self.getLableRobotForLocation(location)
			labelRobot.labelItem(item)

	def listAllItems(self):
		for item in self.items:
			print(item)

if __name__ == "__main__":
	robotFacility = RobotWirehouse()
	item1 = Item('iPhone', None, 'X1Y')
	robotFacility.addItem(item1)
	robotFacility.addItem(Item('Orange Juice', datetime(2018, 6, 20), 'Y1Y'))
	robotFacility.addItem(Item('Vegi Juice', datetime(2019, 6, 20), 'Z3Z'))
	robotFacility.addItem(Item('Samsung S5', None, 'X2A'))
	robotFacility.addItem(Item('School bag', None, 'Y2A'))
	robotFacility.listAllItems()
