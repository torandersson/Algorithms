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
	index = 0
	for number in list:
		if(number <= pivot):
			smaller.append(number)
		elif(number >= pivot):
			bigger.append(number)
	sort_ed = []
	sort_ed.extend(sort(smaller))
	sort_ed.append(pivot)
	sort_ed.extend(sort(bigger))
	return sort_ed


def get_pivot(list):
	first = list[0]
	last = list[len(list)-1]
	#return index
	if first > last:
		return list.pop(0)
	return list.pop(len(list)-1)
	


