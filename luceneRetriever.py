import sys
import lucene
from calcDocDistance import calculateDistance
from lucene import File
from lucene import StandardAnalyzer
from lucene import Document, Field
from lucene import IndexSearcher
from lucene import IndexReader
from lucene import QueryParser
from lucene import SimpleFSDirectory
from lucene import Version
from findMinDistance import findMinDistance
from maxMinDispersion import calculateMaxMin
from findMaxDistance import findMaxDistance
from functionScore import functionScore
from maxCoverage import calculateMaxCoverage
import pickle
import tornado.ioloop
import tornado.web

doc_urls = pickle.load(open("doc_urls.p", "rb"))
new_urls = pickle.load(open("new_urls.p", "rb"))
distanceMatrix = pickle.load(open("distances.p", "rb"))
inv_map = dict((v, k) for k, v in doc_urls.iteritems())


def retrieveDocs(q):
    lucene.initVM()
    analyzer = StandardAnalyzer(Version.LUCENE_30)
    reader = IndexReader.open(SimpleFSDirectory(File("index/")))
    searcher = IndexSearcher(reader)
 
    query = QueryParser(Version.LUCENE_30, "text", analyzer).parse(q)
    MAX = 1000
    hits = searcher.search(query, MAX)
    nonDiverse = []
    docsToScores = {}
        #create a list of html files with relevant websites
    rQ = []
    print "Found %d document(s) that matched query '%s':" % (hits.totalHits, query)
    for hit in hits.scoreDocs:
        print hit.score, hit.doc, hit.toString()
        doc = searcher.doc(hit.doc)
        print doc.get("text").encode("utf-8")
        #print(new_urls[str(hit.doc)])
        result = str(hit.score)+ " " + str(hit.doc) + " " + hit.toString()
        if (len(nonDiverse)<10):
            nonDiverse.append(new_urls[str(hit.doc)])
        #find the document that corresponds to the html website and append to a list for min distance
        website = new_urls[str(hit.doc)]
        #html_files numbers of the hit websites added to rQ
        rQ.append(inv_map[website])
        docsToScores[int(inv_map[website])] = hit.score
        print(inv_map[website])
    return docsToScores, rQ, nonDiverse
