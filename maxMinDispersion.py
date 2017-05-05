from findMaxDistance import findMaxDistance
from findMinPrimeDistance import findMinPrimeDistance

def calculateMaxMin(U, k, parameter, docsToScores):
	distancesToS = {}
	U = set(U)
	S = set()
	maxarg, u, v = findMaxDistance(U, int(parameter), docsToScores)
	S.add(u)
	S.add(v)
	print("U and V")
	print(u)
	print(v)
	for x in U.difference(S):
		distancesToS[x] = findMinPrimeDistance(U.difference(S), x, int(parameter), docsToScores)
		print(distancesToS[x])
		
	