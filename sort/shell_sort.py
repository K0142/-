# Shell Sort - 오름차순
def insert_sort(array, first, last, h):
	i = first + h
	while i <= last:
		val = array[i]
		pos = i
		while pos > first and array[pos-h] > val:
			array[pos] = array[pos-h]
			pos -= h
		array[pos] = val
		i += h
	return array

def shell_sort(array):
	size = len(array)
	h = size // 2
	while h > 0:
		for i in range(h):
			insert_sort(array, i, size-1, h)
		h = h // 2
	return h

array = [322, 110, 127, 58, 12, 467]
shell_sort(array)
print(array)
