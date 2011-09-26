"""Implementation of the quicksort n log(n) algorithm
 
Divide and conquer

example run...with random list

import random 
unsorted_list = []
for count in range(1,1100):
	unsorted_list.append(count)
	
unsorted_list = random.shuffle(unsorted_list)
sorted_list = sort(unsorted_list)

#print the result
for number in sorted_list:
	print number


"""


def sort(list):
	if len(list) == 0 or len(list) == 1:
		return list
	pivot = get_pivot(list)
	smaller = []
	bigger = []
	for number in list:
		if(number <= pivot):
			smaller.append(number)
		elif(number > pivot):
			bigger.append(number)
	result = []
	result.extend(sort(smaller))
	result.append(pivot)
	result.extend(sort(bigger))
	return sort_ed


#need to change this into a better pivot picker.
def get_pivot(list):
	first = list[0]
	last = list[len(list)-1]
	#return index
	if first > last:
		return list.pop(0)
	return list.pop(len(list)-1)
	


