# heap 성질을 만족하도록 하는 연산
def heapify(array, idx, size):
	max_idx  = idx
	left = 2 * idx + 1
	right = 2 * idx + 2

	if left < size and array[left] > array[max_idx]:
		max_idx = left
	if right < size and array[right] > array[max_idx]:
		max_idx = right
	
	if max_idx != idx:
		array[max_idx], array[idx] = array[idx], array[max_idx]
		heapify(array, max_idx, size)

def heap_sort(array):
	a_size = len(array)
	for i in range(a_size // 2 - 1, -1, -1):
		heapify(array, i, a_size)

	for i in range(a_size - 1, 0, -1):
		array[0], array[i] = array[i], array[0]
		heapify(array, 0, i)

	return array

array = [3, 5, 9, 1, 4, 2]
heap_sort(array)
print(array)
