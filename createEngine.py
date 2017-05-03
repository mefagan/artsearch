import subprocess

def createEngine():
    p3 = subprocess.call(["python3", "run.py"])
    #p3.wait()
    p4 = subprocess.call(["python2.6", "testRetriever.py"])
    #p4.wait()
    # 90 is the timeout in seconds
    #try:
     #   out_3, errs_3 = p3.communicate(timeout=400)
    
    #except subprocess.TimeoutExpired:
     #   p3.kill()
      #  out_3, errs_3 = p1.communicate()
    
  #  try:
   #     out_4, errs_4 = p4.communicate(timeout=90)
    #except subprocess.TimeoutExpired:
     #   p4.kill()
      #  out_4, errs_4 = p4.communicate()
def main():
    createEngine()
if __name__ == '__main__':
    main()

