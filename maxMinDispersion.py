doc_urls = pickle.load(open("doc_urls.p", "rb"))
distanceMatrix = pickle.load(open("distances.p", "rb"))

def calculateMaxMin(U, k, scores):
	setS = []
	maxArg = 0
	for doc1 in U:
		for doc2 in U:
			if doc1 != doc2:
				score = functionScore(doc1, doc2)
				docs = doc1, doc2

				if score > maxArg:
					maxArg = score