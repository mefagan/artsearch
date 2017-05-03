#! /usr/bin/env/python3
#robot code taken from https://docs.python.org/2/library/robotparser.html
#crawler code taken from http://www.netinstructions.com/how-to-make-a-web-crawler-in-under-50-lines-of-python-code/
#domain code found on http://stackoverflow.com/questions/14625693/find-http-and-or-www-and-strip-from-domain-leaving-domain-com
#http://stackoverflow.com/questions/4776924/how-to-safely-get-the-file-extension-from-a-url

import pathlib
import sys
from urllib import robotparser
import urllib.request
from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse
from urllib.parse import urlparse
from urllib.parse import urljoin
from url_normalize import url_normalize
import pickle
doc_urls = {}


class LinkParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    newUrl = parse.urljoin(self.baseUrl, value)
                    self.links = self.links + [newUrl]


    def getLinks(self, url):
        self.links = []
        self.baseUrl = url
        response = urlopen(url)
        if response.getheader('Content-Type')=='text/html' or response.getheader('Content-Type')=='text/htm' or response.getheader('Content-Type')=='text/html; charset=UTF-8' or response.getheader('Content-Type')=='text/htm; charset=UTF-8':
            htmlBytes = response.read()
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return htmlString, self.links
        else:
            return "",[]

def checkRobots(url):
    rp = robotparser.RobotFileParser()
    rp.set_url(urljoin(url, 'robots.txt'))
    rp.read()
    return rp.can_fetch("*", url)

def spider(url, maxPages, domain):
    crawled = []
    src_dir = "html_files"
    pagesToVisit = [url]
    numberVisited = 0
    while len(doc_urls) < maxPages and pagesToVisit != []:
        numberVisited = numberVisited +1
        url = url_normalize(pagesToVisit[0])
        parsed_domain_url = urlparse(domain)
        parsed_url = urlparse(url)
        if domain.startswith('http'):
            domain = parsed_domain_url.netloc
        else:
            domain = parsed_domain_url.path
        if url.startswith('http'):
            search_domain = parsed_url.netloc
        else:
            search_domain = parsed_url.path
        robot_url = pagesToVisit[0]
        pagesToVisit = pagesToVisit[1:]
        i = 0
        try:
            if checkRobots(robot_url) and url not in crawled and domain in search_domain:
                print(numberVisited, "Visiting:", url)
                parser = LinkParser()
                data, links = parser.getLinks(url)
                urllib.request.urlcleanup()
                #f = urllib.urlopen(str(url))
                urllib.request.urlretrieve(url, "html_files/" + str(len(crawled)))
                print(str(len(crawled)))
                doc_urls[str(len(crawled))] = url
                crawled.append(url)
                pagesToVisit = pagesToVisit + links
                print(" **Success!**")
                i = i+1

            else:
                if not checkRobots(robot_url):
                    print ("Robot exclusion forbids crawling this page", url)
                if url in crawled:
                    print("crawl already contains", url)
                if not domain in search_domain:
                    print("outside domain", url)
        except:
            print(" **Failed!**")


def main():
    spider(sys.argv[1], int(sys.argv[2]), sys.argv[3])
    pickle.dump(doc_urls, open("doc_urls.p","wb"), protocol=2)
if __name__ == '__main__':
    main()
