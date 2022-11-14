# Sequential Search 함수
def sequential_search(array, value):
	size = len(array)
	for i in range(0, size):
		if value == array[i]:
			return i
	return -1   # 끝까지 비교해서 데이터가 없으면 -1 반환

array = [17, 92, 18, 44, 58, 7, 33, 42]
print("18 검색 => ", sequential_search(array, 18))
print("33 검색 => ", sequential_search(array, 33))
print("100 검색 => ", sequential_search(array, 100))
