from findMaxDistance import findMaxDistance

def calculateMaxMin(U, k, parameter, docsToScores):
	U = set(U)
	S = set()
	maxarg, u, v = findMaxDistance(U, int(parameter), docsToScores)
	S.add(u)
	S.add(v)
	print("U and V")
	print(u)
	print(v)
	for x in U.difference(S):
		print(x)
	