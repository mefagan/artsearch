import lucene
from indexer import createIndex
from lucene import \
    SimpleFSDirectory, System, File, \
    Document, Field, StandardAnalyzer, IndexSearcher, Version, QueryParser

import pickle
doc_urls = pickle.load(open("doc_urls.p", "rb"))

def query(query):
    lucene.initVM()
    indexDir = "/Tmp/REMOVEME.index-dir"
    dir = SimpleFSDirectory(File(indexDir))
    analyzer = StandardAnalyzer(Version.LUCENE_30)
    searcher = IndexSearcher(dir)
    
    query = QueryParser(Version.LUCENE_30, "text", analyzer).parse(query)
    MAX = 1000
    hits = searcher.search(query, MAX)
    
    print "Found %d document(s) that matched query '%s':" % (hits.totalHits, query)
    for hit in hits.scoreDocs:
        print hit.score, hit.doc, hit.toString(), doc_urls[str(hit.doc)]
        doc = searcher.doc(hit.doc)
        #print doc.get("text").encode("utf-8")

def main():
    createIndex()
    query()
if __name__ == '__main__':
    main()
