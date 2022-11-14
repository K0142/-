# Quick Sort 메소드
def quick_sort(array, start, end):
	size = len(array)
	if size <= 1:
		return array
	pivot = start
	left = start + 1
	right = end
	while(left <= right):
		# pivot보다 큰 데이터를 찾을 때까지
		while(left <= end and array[left] <= array[pivot]):
			left += 1
		# pivot보다 작은 데이터를 찾을 때까지
		while(right > start and array[right] >= array[pivot]):
			right -= 1
		if(left > right):  # 엇갈렸다면 작은 데이터와 pivot을 교환
			array[right], array[pivot] = array[pivot], array[right]
		else:              # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교환
			array[left], array[right] = array[right], array[left]
		
		quick_sort(array, start, right - 1)
		quick_sort(array, right + 1, end)

array = [3, 5, 13, 9, 1, 4, 10, 2]
quick_sort(array, 0, len(array)-1)
print(array)
