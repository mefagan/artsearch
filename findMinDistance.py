#assumes set size is larger than 1
def findMinDistance(S):
	minDistance = calcDocDistance(S[0],S[1])
	for doc1 in S:
		for doc2 in S:
			if doc1 != doc2:
				dist = calcDocDistance(doc1, doc2)
				if dist < minDistance:
					minDistance = dist
	return minDistance
