# project is to sort a list
# list: 1 5 3 7 

unsorted = [1, 3, 7, 99, 2]

sort = []

while unsorted:
	minimum = unsorted[0]
	for n in unsorted:
		number = min(unsorted)
		unsorted.remove(number)
		sort.append(number)
	
print sort


