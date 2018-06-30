def a():
	print('a called')
	b()
def b():
	print('b called')
	c()
def c():
	try:
		a = []
		a[0]
	except IndexError:
		print('Index error occurred')
	print('c called')

a()
