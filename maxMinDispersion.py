from findMaxDistance import findMaxDistance
from findMinPrimeDistance import findMinPrimeDistance
import operator
from collections import defaultdict

def calculateMaxMin(U, k, parameter, docsToScores):
	distancesToS = defaultdict(list)
	U = set(U)
	S = set()
	maxarg, u, v = findMaxDistance(U, int(parameter), docsToScores)
	S.add(u)
	S.add(v)
	distancesToSList = []

	for x in U.difference(S):
		mindistance = findMinPrimeDistance(U.difference(S), x, int(parameter), docsToScores)
		distancesToS[mindistance].append(x)
		if mindistance not in distancesToSList:
			distancesToSList.append(mindistance)

	
	distancesToSList.sort()
	
	i = len(distancesToSList) - 1
	

	while len(S) < int(k) and i > -1:
		dist = distancesToSList[i]
		print(dist)
		i = i-1
		for x in distancesToS[dist]: 
			if (len(S)< int(k)):
				S.add(x)

	print("final length of the set")
	print(len(S))
	return S
	
		
	