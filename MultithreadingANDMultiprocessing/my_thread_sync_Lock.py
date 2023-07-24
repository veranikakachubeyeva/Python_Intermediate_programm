#Multithreading/processing: 
#Write a Python script my_thread_sync.py which will have two threads 
# (apart from main thread) printing numbers from 1 to 100 (inclusively). 
#  The first thread must print only even numbers, the second thread must print only odd numbers. 
# They must print numbers one after another so you will get correct sequence: 


import threading


even_lock = threading.Lock()
odd_lock = threading.Lock()
odd_lock.acquire()


def print_number(start, lock_obg1, lock_obg2):
    for num in range(start, 101, 2):             
        lock_obg1.acquire()       
        print(num)        
        lock_obg2.release()


if __name__ == "__main__":    
          
    t1 = threading.Thread(target=print_number, args=(1, even_lock, odd_lock))
    t2 = threading.Thread(target=print_number, args=(2, odd_lock, even_lock)) 
 
    t1.start()
    t2.start()
 
    t1.join()
    t2.join()