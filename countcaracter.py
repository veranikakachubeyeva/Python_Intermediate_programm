from collections import Counter
import sys


filePath = sys.argv[1]
f = None


try:
    f = open(filePath, "rb")
    d = f.read()
    text = d.decode("utf8", errors="ignore")
    counter = Counter(text).most_common(10)
    print("COUNTER", counter)
    for key in counter:
        print(repr(key[0]), "=>", key[1], "times")   
    f.close()
except:
    f.close()
finally:
    f.close()
    
    
