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
           '</form></body></html>')

    def post(self):

        if self.get_argument("rBased", None) != None:
            q = self.get_argument("query")
            docsToScores, rQ, nonDiverse = retrieveDocs(q)
            self.render("index.html", title="Results", items=nonDiverse, query=q)
        
        if self.get_argument("dBased", None) != None:
            q = self.get_argument("query")
            docsToScores, rQ, nonDiverse = retrieveDocs(q)
            distanceBased = calculateMaxMin(rQ, 10, .7, docsToScores)
            dBased = []
            for x in distanceBased:
                dBased.append(doc_urls[x])
            self.render("index.html", title="Results", items=dBased, query=q)
        
        if self.get_argument("cBased", None) != None:
            q = self.get_argument("query")
            docsToScores, rQ, nonDiverse = retrieveDocs(q)
            coverageBased = calculateMaxCoverage(rQ, 10, .7, docsToScores)
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
