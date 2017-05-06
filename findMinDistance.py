#assumes set size is larger than 1
from calcDocDistance import calculateDistance
import os
def findMinDistance(S):
	src_dir = "html_files"
	minDistance = float('inf')
	distanceMatrix = [[0 for x in range(200)] for y in range(200)] 
	for doc1 in S:
		one = doc1
		print(int(one))
		doc1 = os.path.join(src_dir, doc1)
		print(doc1)
		for doc2 in S:
			two = doc2
			doc2 = os.path.join(src_dir, doc2)
			print(doc2)
	 		if doc1 != doc2 and distanceMatrix[int(one)][int(two)]==0:
	 			dist = calculateDistance(doc1, doc2)
	 			print(dist)
	 			distanceMatrix[int(one)][int(two)] = dist
	 			distanceMatrix[int(two)][int(one)] = dist
	 			if dist < minDistance and dist>0:
					minDistance = dist
	
	return distanceMatrix
