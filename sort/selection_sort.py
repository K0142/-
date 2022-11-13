# Selection Sort 메소드
def sel_sort(array):
	size = len(array)
	for i in range(0, size-1):
		min_idx = i
		for j in range(i+1, size):
			if array[j] < array[min_idx]:
				min_idx = j
			array[i], array[min_idx] = array[min_idx], array[i]
			print("<정렬 과정>", array, end = "\n")

array = [69, 10, 30, 2, 16, 8, 31, 22]
sel_sort(array)
print(array)
