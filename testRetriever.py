import sys
import lucene
 
from lucene import File
from lucene import StandardAnalyzer
from lucene import Document, Field
from lucene import IndexSearcher
from lucene import IndexReader
from lucene import QueryParser
from lucene import SimpleFSDirectory
from lucene import Version
import pickle
import tornado.ioloop
import tornado.web

doc_urls = pickle.load(open("doc_urls.p", "rb"))
new_urls = pickle.load(open("new_urls.p", "rb"))
 
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
        MAX = 10
        hits = searcher.search(query, MAX)
        items = []
        print "Found %d document(s) that matched query '%s':" % (hits.totalHits, query)
        for hit in hits.scoreDocs:
            print hit.score, hit.doc, hit.toString()
            doc = searcher.doc(hit.doc)
            print doc.get("text").encode("utf-8")
            #print(new_urls[str(hit.doc)])
            result = str(hit.score)+ " " + str(hit.doc) + " " + hit.toString()
            items.append(new_urls[str(hit.doc)])

        self.render("index.html", title="Results", items=items, query=q)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
