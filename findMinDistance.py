#assumes set size is larger than 1
from calcDocDistance import calculateDistance
import os
def findMinDistance(S):
	src_dir = "html_files"
	minDistance = float('inf')
	for doc1 in S:
		doc1 = os.path.join(src_dir, doc1)
		for doc2 in S:
			doc2 = os.path.join(src_dir, doc2)
	 		if doc1 != doc2:
	 			dist = calculateDistance(doc1, doc2)
	 			if dist < minDistance:
					minDistance = dist
	return minDistance
