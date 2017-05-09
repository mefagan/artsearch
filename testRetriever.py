
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
from luceneRetriever import retrieveDocs
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
 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body><form action="/" method="post">'
           '<p>Search for query here.</p>'
           '<input type="text" name="query" value="type query here">'
           '<br>'
           '<br>'
           '<input type="submit" name="rBased" value="Relevance-based search">'
           '<br>'
           '<input type="submit" name="dBased" value="Distance-based search">'
           '<br>'
           '<input type="submit" name="cBased" value="Coverage-based search">'
           '<p>This is a search engine that searches within 200 crawled pages of the Wikipedia domain. It has two options for diversifying search results.</p>'
           '<p> The first option is a standard relevance-based search, which uses the Lucene package to index and score documents.</p>'
          ' <p> The second option is a distance-based search, which implements the MaxMinDispersion algorithm described at http://www.ambuehler.ethz.ch/CDstore/www2009/proc/docs/p381.pdf. This favors extreme documents. The documents in this cluster are far from each other, but relevant to the query</p>'
           '<p> The third option is a coverage-based search, which implements the MaxCoverage algorithm found at http://journal.webscience.org/368/2/websci10_submission_73.pdf. This ensures all relevant documents in a cluster are close to some chosen document.</p>'
           '</form></body></html>')

    def post(self):

        if self.get_argument("rBased", None) != None:
            q = self.get_argument("query")
            docsToScores, rQ, nonDiverse = retrieveDocs(q)
            self.render("index.html", title="Results", items=nonDiverse, query=q)
        
        if self.get_argument("dBased", None) != None:
            q = self.get_argument("query")
            docsToScores, rQ, nonDiverse = retrieveDocs(q)
            distanceBased = calculateMaxMin(rQ, 10, 5, docsToScores)
            dBased = []
            for x in distanceBased:
                dBased.append(doc_urls[x])
            self.render("index.html", title="Results", items=dBased, query=q)
        
        if self.get_argument("cBased", None) != None:
            q = self.get_argument("query")
            docsToScores, rQ, nonDiverse = retrieveDocs(q)
            coverageBased = calculateMaxCoverage(rQ, 10, 5, docsToScores)
            cBased = []
            for x in coverageBased:
                cBased.append(doc_urls[x])
            self.render("index.html", title="Results", items=cBased, query=q)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
  
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
