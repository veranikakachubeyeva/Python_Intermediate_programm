#Multithreading/processing: 
#Write a Python script my_thread_sync.py which will have two threads 
# (apart from main thread) printing numbers from 1 to 100 (inclusively). 
#  The first thread must print only even numbers, the second thread must print only odd numbers. 
# They must print numbers one after another so you will get correct sequence: 


import threading


even_lock = threading.Lock()
odd_lock = threading.Lock()
odd_lock.acquire()

def func_print_even_numbers():           
    for num in range(2, 101, 2):             
        odd_lock.acquire()       
        print(num)        
        even_lock.release()


def func_print_odd_numbers():            
    for num in range(1, 100, 2):         
        even_lock.acquire()
        print(num)                
        odd_lock.release()

if __name__ == "__main__":    
          
    t1 = threading.Thread(target=func_print_even_numbers)
    t2 = threading.Thread(target=func_print_odd_numbers) 
 
    t1.start()
    t2.start()
 
    t1.join()
    t2.join()