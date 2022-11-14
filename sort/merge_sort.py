# Merge Sort 메소드
def merge_sort(array):
	if len(array) < 2:
		return array

	mid = len(array) // 2
	low_array = merge_sort(array[:mid])
	high_array = merge_sort(array[mid:])

	l = h = k = 0
	while l <len(low_array) and h < len(high_array):
		if low_array[l] < high_array[h]:
			array[k] = low_array[l]
			l += 1
		else: 
			array[k] = high_array[h]
			h += 1
		k += 1
	while l < len(low_array):
		array[k] = low_array[l]
		l += 1
		k += 1

	while h < len(high_array):
		array[k] = high_array[h]
		h += 1
		k += 1
	return array

array = [68, 9, 30, 2, 16, 8, 32, 20]
merge_sort(array)
print(array)
