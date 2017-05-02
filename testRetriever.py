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
 
if __name__ == "__main__":
    lucene.initVM()
    analyzer = StandardAnalyzer(Version.LUCENE_30)
    reader = IndexReader.open(SimpleFSDirectory(File("index/")))
    searcher = IndexSearcher(reader)
 
    query = QueryParser(Version.LUCENE_30, "text", analyzer).parse("art")
    MAX = 1000
    hits = searcher.search(query, MAX)
 
    print "Found %d document(s) that matched query '%s':" % (hits.totalHits, query)
    for hit in hits.scoreDocs:
        print hit.score, hit.doc, hit.toString()
        doc = searcher.doc(hit.doc)
        print doc.get("text").encode("utf-8")
