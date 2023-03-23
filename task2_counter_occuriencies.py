# Write a simple program which counts the maximum number of occuriencies of one byte in a row in file.
# For example, processing b"aabbbaaaacc" (taken from file arg) returns ("a", 4) as result.

import sys


def  get_data_from_file(file):
    if len(file) != 2:
        print ("Usage: python pythonfile.py textfile.txt")
        sys.exit()

    filePath = file[1]

    with open(filePath, "rb") as f:
        d = f.read()
        return d
    

def count_occuriencies (input_data):
    if len(input_data)==0:
        return None
    
    
    list_of_seq = []
    result_statment = set() 
    max_len = 1
    current_len = 0 
    current_char = input_data[0]
    
    
    for item in input_data:
        if item == current_char:
            current_len += 1
            max_len = current_len
        else:
            if current_len > 0:
                    
                if max_len < current_len:
                    max_len = current_len 
                list_of_seq.append((chr(current_char), current_len))     
                
            current_len = 1
            current_char = item
    
   
    list_of_seq.append((chr(current_char), current_len))
    
        
    result = list(filter(lambda x: x[1] == max_len, list_of_seq))   
    
    
    for  el in result:
        result_statment.add(el)
                  
    return result_statment
