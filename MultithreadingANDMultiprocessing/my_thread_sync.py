#Multithreading/processing: 
#Write a Python script my_thread_sync.py which will have two threads 
# (apart from main thread) printing numbers from 1 to 100 (inclusively). 
#  The first thread must print only even numbers, the second thread must print only odd numbers. 
# They must print numbers one after another so you will get correct sequence: 

import threading
import time

max_number = 100

barrier = threading.Barrier(2)

def print_even_numbers():
    for i in range(2, max_number + 1, 2):               
        time.sleep(0.1)
        barrier.wait()
        print(i)
        print("//////////")

def print_odd_numbers():
    for i in range(1, max_number + 1, 2):            
        time.sleep(0.2)
        print(i)        
        barrier.wait()
        print("*************") 


if __name__ == "__main__":
    
    t1 = threading.Thread(target=print_odd_numbers)
    t2 = threading.Thread(target=print_even_numbers)
    
    t1.start()
    t2.start()             
        
    t1.join()
    t2.join()