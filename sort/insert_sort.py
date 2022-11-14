# Insert Sort 메소드
def insert_sort(array):
	size = len(array)
	for i in range(1, size):
		for j in range(i, 0, -1):
			if array[j-1] > array[j]:
				array[j-1], array[j] = array[i], array[i-1]
			else:
				break
	return

array = [58, 12, 127, 322, 110, 467]
insert_sort(array)
print(array)	
	
