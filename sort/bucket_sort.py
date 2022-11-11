def bucket_sort(num):
	# 버킷을 담을 list 생성한다.
	bucket_list = [[] for _ in range(len(num))]

	# 버킷에 각 값을 넣는다.
	for n in num:
		index = int(len(num)*n)
		bucket_list[index].append(n)

	for end in range(1, len(num)):
		for i in range(end, 0, -1):
			if bucket_list[i-1] > bucket_list[i]:
				bucket_list[i-1], bucket_list[i] = bucket_list[i], bucket_list[i-1]

	# 각 버킷을 연결한다.
	k = 0
	for i in range(len(num)):
		for j in range(len(bucket_list[i])):
			num[k] = bucket_list[i][j]
			k += 1
	return num

num_list = [0.88, 0.07, 0.39, 0.46, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68] 
print(num_list)

bucket_list = bucket_sort(num_list)
print(bucket_list) 
