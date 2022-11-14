# Binary Search 함수
def binary_search(array, target):
	array.sort()
	start = 0
	end = len(array) - 1
	
	while start <= end:
		mid = (start + end) // 2
		if array[mid] == target:
			return mid
		elif array[mid] > target:
			end = mid - 1
		else: 
			start = mid + 1
	return None

array = [1, 3, 4, 5, 7, 8, 9 , 10]
print("3 검색 => ", binary_search(array, 3))
