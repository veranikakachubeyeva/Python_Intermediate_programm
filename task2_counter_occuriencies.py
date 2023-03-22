# Write a simple program which counts the maximum number of occuriencies of one byte in a row in file.
# For example, processing b"aabbbaaaacc" (taken from file arg) returns ("a", 4) as result.

import sys


def  open_file(file):
    if len(file) != 2:
        print ("Usage: python pythonfile.py textfile.txt")
        sys.exit()

    filePath = file[1]

    with open(filePath, "rb") as f:
        d = f.read()
        return d
    

def count_occuriencies (input_data):
    if len(input_data)==0:
        return set()
    
    
    max_count = 0
    current_count = 0
    current_byte_element = input_data[0]
    list_of_seq = []
    result_statment = set()
    
        
    for index in range(len(input_data)):
        if (input_data[index] == current_byte_element):
                current_count += 1        
                
        if (input_data[index] != current_byte_element) or ((current_byte_element == input_data[index]) and (index == len(input_data)-1)):
            
            if current_count > 0:
                    
                if max_count < current_count:
                    max_count = current_count                   
                       
                list_of_seq.append((chr(current_byte_element), current_count))
            current_byte_element = input_data[index] 
            current_count = 1
            
            
        if (current_byte_element == input_data[index]) and (index == len(input_data)-1):
            
            if current_count > 0:
                    
                if max_count < current_count:
                    max_count = current_count                    
                       
                list_of_seq.append((chr(current_byte_element), current_count))
            current_byte_element = input_data[index] 
            current_count = 1
               
            
    result = list(filter(lambda x: x[1] == max_count, list_of_seq))    
    
    for  el in result:
        result_statment.add(el)
                  
    return result_statment
  