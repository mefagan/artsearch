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
from functionScore import functionScore
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
           '<input type="submit" value="Submit">'
           '</form></body></html>')
    def post(self):
        q= self.get_argument("query")

        lucene.initVM()
        analyzer = StandardAnalyzer(Version.LUCENE_30)
        reader = IndexReader.open(SimpleFSDirectory(File("index/")))
        searcher = IndexSearcher(reader)
 
        query = QueryParser(Version.LUCENE_30, "text", analyzer).parse(q)
        MAX = 1000
        hits = searcher.search(query, MAX)
        items = []
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
            if (len(items)<10):
                items.append(new_urls[str(hit.doc)])
            #find the document that corresponds to the html website and append to a list for min distance
            website = new_urls[str(hit.doc)]
            #html_files numbers of the hit websites added to rQ
            rQ.append(inv_map[website])
            docsToScores[int(inv_map[website])] = hit.score
            print(inv_map[website])
        score = functionScore(99, 151, .7, docsToScores)
        print("DISTANCE MATRIX")
        print(distanceMatrix[int(99)][int(151)])
        print(docsToScores[int(99)])
        print(docsToScores[int(151)])
        print("SCORE")
        print(score)

        #distanceMatrix[][]
    
        

        self.render("index.html", title="Results", items=items, query=q)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
