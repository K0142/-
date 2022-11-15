# skip 배열 생성
def init_skip(pattern):
	num = 27
	p_size = len(pattern)
	skip = [p_size for i in range(num)]
	
	for i in range(p_size):
		skip[ord(pattern[i]) - ord('A')] = p_size - i - 1
	return skip

# BM 
def bm(pattern, all_str):
	p_size = len(pattern)
	s_size = len(all_str)
	skip = init_skip(pattern)

	j = p_size - 1
	i = s_size - 1
	while j >= 0:
		while all_str[i] != pattern[j]:
			k = skip[ord(all_str[i]) - ord('A')]
			if p_size - j > k:
				i = i + p_size - j
			else:
				i = i + k
			if i >= s_size:
				return s_size
			j = p_size - 1
		i = i - 1
		j = j - 1
	return i + 1

print(bm("ATION", "VISOINQUESTIONONIONCAPTIONGRADUATION"))
