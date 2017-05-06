from calcDocDistance import calculateDistance
import pickle
import os
distanceMatrix = pickle.load(open("distances.p", "rb"))
def calculateCoverageError(U):
	coverageErrors = {}
	for doc1 in U: 
		minDistance = float('inf')
		for doc2 in U:
	 		if doc1 != doc2: 
	 			dist = distanceMatrix[int(doc1)][int(doc2)]
	 			if dist < minDistance and dist> -1:
					minDistance = dist
		coverageErrors[int(doc1)] = minDistance
	return coverageErrors
