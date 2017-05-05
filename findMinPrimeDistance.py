from functionScore import functionScore
import math
def findMinPrimeDistance(set, docx, parameter, docsToScore):
	minArg = float('inf')
	for docu in set:
		#compare the document x to each other document, compute score, and find min
		if docx != docu:
			score = functionScore(docx, docu, parameter, docsToScore)
			if score < minArg and score != 0:
				minArg = score
	
	return minArg