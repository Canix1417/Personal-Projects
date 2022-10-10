import random

def selection_sort(unsorted_list) -> []:
	sorted_list = []	
	
	for x in range(len(unsorted_list)):
		lowest_index = 0
		lowest_value = unsorted_list[0]
		for y in range(1, len(unsorted_list)):
			current_value = unsorted_list[y]
			if current_value < lowest_value:
				lowest_index = y
				lowest_value = current_value
	
		sorted_list.append(unsorted_list.pop(lowest_index))
		
	return sorted_list

#def merge_sort():
  
#def merge_sort_recursive() -> list[int]:

#def bubble_sort() -> :

#def bubble_sort_recursive() ->:

#def quick_sort()  ->:

#def quick_sort_recursive() ->:

list_one = random.sample(range(1, 100), 12)
#list_two = sort(random.sample(range(1,100), 12))

print("The unsorted list is: " + str(list_one))
print("The selection sorted version of the list  is: " + str(selection_sort(list_one)))
print("The quick sorted version of the list is: ")
print("The sorted version of the list is: ")
print("The sorted version of the list is: ")
