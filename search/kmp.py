# KMP
def kmp(all_str, pattern):
	# kmp table
	table = [0 for _ in range(len(pattern))]
	i = 0
	for j in range(1, len(pattern)):
		while i > 0 and pattern[i] != pattern[j]:
			i = table[i-1]

		if pattern[i] == pattern[j]:
			i += 1
			table[j] = i

	# kmp
	result = []
	i = 0
	for j in range(len(all_str)):
		while i > 0 and pattern[i] != all_str[j]:
			i = table[i-1]
		
		if pattern[i] == all_str[j]:
			i += 1
			if i == len(pattern):
				result.append(j-i+1)
				i = table[i-1]
	return result

print(kmp('xabxxbaxbaxbaxbaxabxbaxbabx', 'abx'))
print(kmp('abababab', 'abab'))
