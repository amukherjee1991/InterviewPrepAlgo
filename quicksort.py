def quicksort(array):
	if len(array)<=1:
		return array
	else:
		pivot=array.pop()
	greater=[]
	lower=[]

	for items in array:
		if items > pivot:
			greater.append(items)
		else:
			
			lower.append(items)
	return quicksort(lower)+[pivot]+ quicksort(greater)


def selectionsort(array):
	indexing_length=range(len(array))

	for i in indexing_length:
		min_val=i
		for j in range(i+1,len(array)):
			if array[j]<array[min_val]:
				min_val=j
		if min_val!=i:
			array[min_val],array[i]=array[i],array[min_val]

	return array


def bubblesort(array):
	indexing_length=len(array)-1
	sorted=False

	while not sorted:
		sorted = True
		for i in range(0,indexing_length):
			if array[i]>array[i+1]:
				sorted=False
				array[i],array[i+1]=array[i+1],array[i]
	return array

array_1=[45,74,1,647,1089,-1]

def insertion_sort(array):
	indexing_length=range(1,len(array))
	for i in indexing_length:
		val_to_sort=array[i]
		while array[i-1]>val_to_sort and i > 0:
			array[i],array[i-1]=array[i-1],array[0]
			i-=1
	return array


# print quicksort(array_1)

print insertion_sort(array_1)
print selectionsort(array_1)

print bubblesort(array_1)