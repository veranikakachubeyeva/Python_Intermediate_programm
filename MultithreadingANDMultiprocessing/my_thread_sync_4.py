#Multithreading/processing: 
#Write a Python script my_thread_sync.py which will have two threads 
# (apart from main thread) printing numbers from 1 to 100 (inclusively). 
#  The first thread must print only even numbers, the second thread must print only odd numbers. 
# They must print numbers one after another so you will get correct sequence: 


import threading

max_number = 100
current_number = 1

event = threading.Event()

def predicate(i):       
    return i == current_number
       

def print_numbers(start):
    global current_number    
    for i in range(start, max_number + 1, 2):          
        while not predicate(i):
            event.wait()
        print(i)               
        current_number = i + 1         
        event.set()  
        
             
if __name__ == "__main__":        
   
    t1 = threading.Thread(target=print_numbers, args=(1,))
    t2 = threading.Thread(target=print_numbers, args=(2,))
    
    t1.start()
    t2.start()             
        
    t1.join()
    t2.join()
