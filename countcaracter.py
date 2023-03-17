from collections import Counter
import sys
import codecs


filePath = sys.argv[1]


f = open(filePath, "rb")
d = f.read()
text = codecs.decode(d, "utf8", errors="ignore")
counter = dict(Counter(text).most_common(10))
print("COUNTER", counter)

for key in counter:
    print(str(key.encode("utf8"))[1:], "=>", counter[key], "times")
    #print(len(str(key.encode("utf8"))[1:]))


f.close()