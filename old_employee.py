class Employee:
	def __init__(self, name, title, department):
		self.name = name
		self.title = title
		self.department = department

	def getEmployeeInfo(self):
		return 'Name: ' + self.name + ', title: ' + self.title + ', department: ' + self.department


class Permanent(Employee):
	def __init__(self, name, title, department):
		super().__init__(name, title, department)

		def requestVacation(self, startDate, endDate):
			print(super().name + ' has requested a vacation')

class Temporary(Employee):
	def __init__(self, name, title, department, endDate):
		super().__init__(name, title, department)
		self.endDate = endDate

	def getEmployeeInfo(self):
		return super().getEmployeeInfo() + ', End date: ' + self.endDate

class Manger(Permanent):
	def __init__(self, name, title, department):
		super().__init__(name, title, department)
		self.allEmployee = []

	def addEmployee(self, employee):
		self.allEmployee.append(employee)

	def listAllEmployees(self):
		for employee in self.allEmployee:
			print(employee.name)

class TeamLead(Permanent):
	def __init__(self, name, title, department):
		super().__init__(name, title, department)
		self.teamMember = []

	def addTeamMember(self, employee):
		self.teamMember.append(employee)

	def listTeamMembers(self):
		for teamMember in self.teamMember:
			print(teamMember.name)

class Engineer(Permanent):
	def __init__(self, name, title, department):
		super().__init__(name, title, department)

class Intern(Temporary):
	def __init__(self, name, title, department, endDate):
		super().__init__(name, title, department, endDate)

employee1 = Engineer('Bob', 'Software Engineer', 'IT')
employee2 = Engineer('Jon', 'Software Engineer', 'IT')
employee3 = TeamLead('Jane', 'Backend Lead', 'IT')
employee3.addTeamMember(employee1)
employee3.addTeamMember(employee2)
employee3.listTeamMembers()



print(isinstance(employee3, Manger))
print(isinstance(employee3, Engineer))
print(isinstance(employee3, TeamLead))
print(isinstance(employee3, Employee))

print(employee3.getEmployeeInfo())
employee4 = Intern('Ali', 'Junior Python Dev', 'IT', 'Jan 1, 2019')
print(employee4.getEmployeeInfo())
