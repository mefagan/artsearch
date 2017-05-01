#http://stackoverflow.com/questions/9745056/how-to-save-user-input-data-to-redis-using-tornado-python
from stripHTML import strip_tags
from calculateWordScore import calculateWordScore
from removeStopWords import stripStopWords
from getWordsForScoring import getWordsForScoring
from calculateDocScore import calculateDocScore
from calculateKNewWords import calcNewQuery
from calczWQ import calczWQ
import os
import codecs
import tornado.ioloop
import operator
import tornado.web
import pickle
import lucene
from indexer import createIndex
from lucene import \
    SimpleFSDirectory, System, File, \
    Document, Field, StandardAnalyzer, IndexSearcher, Version, QueryParser

doc_urls = pickle.load(open("doc_urls.p", "rb"))

class MainHandler(tornado.web.RequestHandler):
    def get(self):
      self.write('<html><body><form action="/" method="post">'
           '<p>Number of terms for relevance feedback.</p>'
           '<input type="text" name="kTerms" value="0">'
           '<html><body><form action="/" method="post">'
           '<p>Search for query here.</p>'
           '<input type="text" name="query" value="type query here">'
           '<input type="submit" value="Submit">'
           '</form></body></html>')
    def post(self):
      q= self.get_argument("query")
      k =self.get_argument("kTerms")

      # self.write(key)

    # def query(query):
      # query = self.get_argument("q")
      lucene.initVM()
      indexDir = "index"
      dir = SimpleFSDirectory(File(indexDir))
      analyzer = StandardAnalyzer(Version.LUCENE_30)
      searcher = IndexSearcher(dir)
      
      query = QueryParser(Version.LUCENE_30, "text", analyzer).parse(q)
      MAX = 10
      hits = searcher.search(query, MAX)
      
      print "Found %d document(s) that matched query '%s':" % (hits.totalHits, query)
      items = []
      rQ = []
      
      #for key, value in doc_urls.iteritems() 
       # print (key, value)

      for hit in hits.scoreDocs:
          #items.append({'score':hit.score, 'doc':hit.doc, 'blah':hit.toString(), 'url':doc_urls[str(hit.doc)]})
          print hit.score, hit.doc, hit.toString()
          print(len(doc_urls))
          items.append(doc_urls[str(hit.doc)])
          print(doc_urls[str(hit.doc)])
          doc = searcher.doc(hit.doc) 
          print(hit.doc)
          rQ.append("html_files/" + str(hit.doc))
      
      i = 0
      rqSize = 0
      for url in rQ:
        rqSize = rqSize +1
        print(url)
        f=codecs.open(url, 'r')
        html = f.read()
        html = html.decode('utf-8')
        tag_free = strip_tags(html)
        path = 'strippedHTML_files'
        if not os.path.exists(path):
          os.makedirs(path)
        filename = str(i)
        with open(os.path.join(path, filename), 'wb') as temp_file:
          temp_file.write(tag_free.encode('utf-8'))
        i=i+1


      path = 'strippedHTML_files'
      i = 0
      for filename in os.listdir(path):
        with open(os.path.join(path, filename), 'r') as myfile:
          data=myfile.read()
          stripStopWords(data, i)
          i = i+1
      if k>0:
        newQuery = calcNewQuery(k, q, rqSize)
        q = newQuery
        print("new query is ")
        print(q)

      




        
      self.render("index.html", title="Results", items=items, query=q, kTerms = k)






def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
