from findMaxDistance import findMaxDistance
from findMinPrimeDistance import findMinPrimeDistance
import operator

def calculateMaxMin(U, k, parameter, docsToScores):
	distancesToS = {}
	U = set(U)
	S = set()
	maxarg, u, v = findMaxDistance(U, int(parameter), docsToScores)
	S.add(u)
	S.add(v)
	distancesToSList = []
	for x in U.difference(S):
		mindistance = findMinPrimeDistance(U.difference(S), x, int(parameter), docsToScores)
		distancesToS[mindistance] = x
		distancesToSList.append(mindistance)
	distancesToSList.sort()
	i = len(distancesToSList) - 1
	while len(S) < int(k) and i > -1:
		dist = distancesToSList[i]
		x = distancesToS[dist]
		i = i-1
		if dist != float('inf'):
			S.add(x)
	print("final length of the set")
	print(len(S))
	
		
	