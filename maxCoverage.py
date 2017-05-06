from findMaxDistance import findMaxDistance
from findMinPrimeDistance import findMinPrimeDistance
from calculateCoverageErrors import calculateCoverageError
from calculateMaxCoverageScore import calculateMaxCoverageScore
from findMaxScore import findMaxScore
import operator
from collections import defaultdict

def calculateMaxCoverage(U, k, parameter, docsToScores):
	U = set(U)
	S = set()
	maxArg, maxDoc = findMaxScore(U, docsToScores)
	S.add(maxDoc)

	coverageErrors = calculateCoverageError(U)
	scoresDict, scoresList = calculateMaxCoverageScore(U, parameter, coverageErrors, docsToScores)
	scoresList.sort()

	j = len(scoresList)-1
	for i in range(0, k):
		if j > -1:
			doc = scoresDict[scoresList[j]]
			S.add(doc)
		j = j - 1
		i = i +1
	return S