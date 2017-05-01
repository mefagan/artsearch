from bs4 import BeautifulSoup

with open("example1.html") as markup:
    soup = BeautifulSoup(markup.read())

with open("example.txt", "w") as f: 
    f.write(soup.get_text())