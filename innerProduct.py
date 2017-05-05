#taken/adapted from https://courses.csail.mit.edu/6.006/fall11/rec/rec02.pdf
def inner_product(L1, L2):
	sum = 0.0
	for key in L1:
		if key in L2:
			sum = sum + L1[key] * L2[key]
	return sum
