#taken/adapted from https://courses.csail.mit.edu/6.006/fall11/rec/rec02.pdf
def inner_product(L1, L2):
	sum = 0.0
	i = 0
	j = 0
	while i<len(L1) and j<len(L2):
		if L1[i][0] == L2[j][0]:
			#if both lists have the same word then add their product to the sum
			sum += L1[i][1] * L2[j][1]
			i += 1
			j += 1
		elif L1[i][0] < L2[j][0]:
			#word is in the first list but not the second
			i = i+1
		else:
			#word L2[j][0] is in L2 but not L1
			j = j+1
	return sum
