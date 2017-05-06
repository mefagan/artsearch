from functionScore import functionScore
import math
def findMaxScore(rQ, docsToScore):
	maxArg = 0
	maxDoc = float('inf')
	for doc in rQ:
		score = docsToScore[int(doc)]
		if score > maxArg:
			maxArg = score
			maxDoc = doc
	return maxArg, maxDoc