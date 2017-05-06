import pickle
import math
distanceMatrix = pickle.load(open("distances.p", "rb"))

def calculateMaxCoverageScore(U, parameter, coverageErrors, docsToScores):
	scoresDict = {}
	scoresList = []
	for doc in U:
		relScore = docsToScores[int(doc)]
		coverageScore = coverageErrors[int(doc)]
		score = math.pow(relScore, parameter) * coverageScore
		scoresDict[score] = doc
		scoresList.append(score)
	return scoresDict, scoresList

