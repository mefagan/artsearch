from stripHTML import strip_tags
from removeStopWords import stripStopWords
from htmlparser import parsehtml
import os

def cleanUpHTML(): 
  src_dir = "html_files"
  #cycle through every html file and open
  i = 0
  for l in os.listdir(src_dir):
        l = os.path.join(src_dir, l)
        with open(l, 'r') as myfile:
            html=myfile.read()
            html, errors = parsehtml(html)
            html = html.decode('utf-8')
            tag_free = strip_tags(html)
            path = 'strippedHTML_files'
            if not os.path.exists(path):
              os.makedirs(path)
            filename = str(i)
            with open(os.path.join(path, filename), 'wb') as temp_file:
              temp_file.write(tag_free.encode('utf-8'))
            i=i+1
  i = 0
  path = 'strippedHTML_files'
  for filename in os.listdir(path):
    with open(os.path.join(path, filename), 'r') as myfile:
      data=myfile.read()
      stripStopWords(data, i)
      i = i+1