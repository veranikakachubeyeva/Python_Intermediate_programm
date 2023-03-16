from collections import Counter
import sys
#import io

filePath = sys.argv[1]

print(filePath)
print('cmd entry:', sys.argv)
f = open(filePath, "rb")
#f = io.open(filePath, "r")  #, encoding='utf-8')

d = f.read()
print(d)

counter = dict(Counter((d)).most_common(10))
print("COUNTER", counter)

for key in counter:
    #bkey = bytes(key)
    print(key, "=>", counter[key], "times")

f.close()