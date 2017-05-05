import pickle
distanceMatrix = pickle.load(open("distances.p", "rb"))

def functionScore(doc1, doc2, parameter, docsToScore):
	score1 = docsToScore[int(doc1)]
	score2 = docsToScore[int(doc2)]
	distance = distanceMatrix[int(doc1)][int(doc2)]
	return .5*(score1 + score2) + parameter*(distance)

