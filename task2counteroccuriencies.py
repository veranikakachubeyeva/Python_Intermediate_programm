# Write a simple program which counts the maximum number of occuriencies of one byte in a row in file.
# For example, processing b"aabbbaaaacc" (taken from file arg) returns ("a", 4) as result.

import sys


filePath = sys.argv[1]


with open(filePath, "rb") as f:
    d = f.read()
    max_count = 0
    current_count = 0
    current_byte_element = ""
    list_of_seq = []
    
    
    for byte_element in d:
        if byte_element == current_byte_element:
            current_count += 1
            
        else:
            if current_count > 1:
                if max_count < current_count:
                    max_count = current_count
                              
                list_of_seq.append((chr(current_byte_element), current_count))
            current_byte_element = byte_element
            current_count = 1
            
    result = list(filter(lambda x: x[1] == max_count, list_of_seq))    
    
    for  el in result:
        print (el)
    
        
    
    
    
    
    