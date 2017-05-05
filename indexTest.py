from htmlparser import parsehtml
from stripHTML import strip_tags
from removeStopWords import stripStopWords
import sys, threading, time
from datetime import datetime
from findMinDistance import findMinDistance
import lucene
import os
from lucene import SimpleFSDirectory, System, File, Document, Field, StandardAnalyzer, IndexWriter, Version

#from java.nio.file import Paths
from lucene import LimitTokenCountAnalyzer
from lucene import StandardAnalyzer
from lucene import Document, Field #FieldType
from lucene import \
    IndexWriter, IndexWriterConfig
from lucene import SimpleFSDirectory
import pickle
new_urls = {}

doc_urls = pickle.load(open("doc_urls.p", "rb"))



if __name__ == "__main__":
    lucene.initVM()
    src_dir = "html_files"
    indexDir = "index"
    dir = SimpleFSDirectory(File(indexDir))
    analyzer = StandardAnalyzer(Version.LUCENE_30)
    writer = IndexWriter(dir, analyzer, True, IndexWriter.MaxFieldLength(512))
    print ("Currently there are %d documents in the index..." % writer.numDocs())
    print ("Reading lines from directory...")
    i = 0
    for l in os.listdir(src_dir):
        if l.endswith('.DS_Store'):
            continue
        num = int(l)
        l = os.path.join(src_dir, l)
        
        website = doc_urls[str(num)]
        new_urls[str(i)] = website
        print(i, website)
        print(website)
        with open(l, 'r') as myfile:
            data=myfile.read()
            print(l)
        document, errors = parsehtml(data)
        #print(document)
        html = document.decode('utf-8')
        tag_free = strip_tags(html)
        tag_free.encode('utf-8')
        #print(tag_free)
        #stripStopWords(data, i)
        #print(l)
        document = stripStopWords(tag_free, i)
        #print(document)
        i += 1
        #create a list of words in the document
        words = document.split()
        #create a document to add to the index
        doc = Document()
        for word in words:
            #print(word)
            #add a field to the document
            field = Field("text", word.lower(), Field.Store.YES, Field.Index.ANALYZED)
            #add the field to the document
            doc.add(field)
        #add the document to the index
        writer.addDocument(doc)
    print ("Indexed lines from stdin (%d documents in index)" % (writer.numDocs()))
    print ("About to optimize index of %d documents..." % writer.numDocs())
    writer.optimize()
    print ("...done optimizing index of %d documents" % writer.numDocs())
    print ("Closing index of %d documents..." % writer.numDocs())
    writer.close()
    print ("...done closing index of %d documents" % writer.numDocs())
    pickle.dump(new_urls, open("new_urls.p","wb"), protocol=2)
    distanceMatrix = findMinDistance(new_urls)
    pickle.dump(distanceMatrix, open("distances.p", "wb"), protocol=2)