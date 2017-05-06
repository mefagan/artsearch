Pre-computation
createEngine.y
-crawler.py
-indexTest.py

crawler.py
Crawler crawls websites within wikipedia.org starting at root https://en.wikipedia.org/ and stops when there are 200 files that have been crawled and stored. Crawler does not crawl websites that are forbidden to crawl by robot exclusion or are outside the domain. It does not store any links that have already been stored.

indexTest.py
Index test first opens all html files stored at html_files/ and removes all html markup, parses the documents, removes stop words, and returns a list of words for each document. Indexer indexes all 200 pages by indexing each word in the cleaned html files (stripped html markup and stop words, parsed, broken into words). 
