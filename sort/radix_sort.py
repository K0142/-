# Counting Sort를 이용한 공간 할당 함수
def counting_sort(arrat, place):
	size = len(array)
	output = [0]*size   # 배열 크기에 맞는 ouptup 배열 생성 
	count = [0]*10      # 10개의 0을 가진 count 배열 생성

	for i in range(0, size):
		index = int(array[i] / place)
		count[index%10] += 1

	# count 배열 수정
	for i in range(1, 10):
		count[i] += count[i-1]

	# output 배열 설정, 설정된 count 배열의 알맞은 위치에 array 할당
	i = size - 1
	while i >= 0:
		index = int(array[i] / place)
		output[count[index%10]-1] = array[i]
		count[index%10] -= 1
		i -= 1

	# array를 결과물에 재할당
	for i in range(0, len(array)):
		array[i] = output[i]

# Radix Sort 구현 매소드
def radix_sort(array):
	max_value = max(array)
	# 자릿수마다 counting sort 실행
	digit = 1
	while max_value/digit > 0:
		counting_sort(array, digit)
		digit *= 10

array = [121, 432, 564, 23, 1,  45, 788]
radix_sort(array)
print(array)
