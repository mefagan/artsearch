from htmlparser import parsehtml
import lucene
import os
from lucene import SimpleFSDirectory, System, File, Document, Field, StandardAnalyzer, IndexWriter, Version
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
        l = os.path.join(src_dir, l)
        with open(l, 'r') as myfile:
            data=myfile.read()
        document, errors = parsehtml(data)
        print(l)
        i += 1
        doc = Document()
        doc.add(Field("text", document, Field.Store.YES, Field.Index.ANALYZED))
        writer.addDocument(doc)
    print ("Indexed lines from stdin (%d documents in index)" % (writer.numDocs()))
    print ("About to optimize index of %d documents..." % writer.numDocs())
    writer.optimize()
    print ("...done optimizing index of %d documents" % writer.numDocs())
    print ("Closing index of %d documents..." % writer.numDocs())
    writer.close()
    print ("...done closing index of %d documents" % writer.numDocs())