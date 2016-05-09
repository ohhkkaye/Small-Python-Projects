# project is to sort a list
# list: 1 5 3 7 

unsorted = []

sort = []

def sorter(num):
	while num:
		minimum = num[0]
		for n in num:
			number = min(num)
			num.remove(number)
			sort.append(number)
	print sort

def choose():
	print "Hello! We're going to sort numbers."
	print "Please list numbers you would like to add. List 5 numbers one at a time."
	while len(unsorted) < 5:
		number = input("Type: ")
		unsorted.append(number)
	else:
		sorter(unsorted)


choose()
