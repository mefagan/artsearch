from functionScore import functionScore
import math
def findMaxDistance(rQ, parameter, docsToScore):
	maxArg = 0
	for doc1 in rQ:
		for doc2 in rQ:
			if doc1 != doc2:
				score = functionScore(doc1, doc2, parameter, docsToScore)
				print(score)
				if score > maxArg and score != float('inf'):
					maxArg = score
					u = doc1
					v = doc2
	return maxArg, u, v