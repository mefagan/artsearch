#code adapted from http://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
from HTMLParser import HTMLParser
import codecs
import sys

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    parser = HTMLParser()
    s = MLStripper()
    s.feed(html)
    return s.get_data()

#def main():
 #   f=codecs.open(file, 'r')
  #  html = f.read()
   # print(strip_tags(html))
#if __name__ == '__main__':
 #   main()
