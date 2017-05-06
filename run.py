import subprocess

def BuildSearchEngine(url, number, domain):
    p1 = subprocess.call(["python3", "crawler.py", url, str(number), domain])
    p2 = subprocess.call(["python2.6", "indexTest.py"])
    # 90 is the timeout in seconds
    #try:
     #   out_1, errs_1 = p1.communicate(timeout=500)
    
    #except subprocess.TimeoutExpired:
     #   p1.kill()
      #  out_1, errs_1 = p1.communicate()
    
    #try:
     #   out_2, errs_2 = p2.communicate(timeout=180)
    #except subprocess.TimeoutExpired:
     #   p2.kill()
      #  out_2, errs_2 = p2.communicate()

def main():
    BuildSearchEngine("https://en.wikipedia.org/", 200, "wikipedia.org")
if __name__ == '__main__':
    main()
