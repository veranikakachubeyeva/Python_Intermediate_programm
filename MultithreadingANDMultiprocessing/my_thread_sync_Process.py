import multiprocessing 


even_lock = multiprocessing.Lock()
odd_lock = multiprocessing.Lock()
odd_lock.acquire()


def print_number(start, lock_obg1, lock_obg2):
    for num in range(start, 101, 2):             
        lock_obg1.acquire()       
        print(num)        
        lock_obg2.release()
  

if __name__ == '__main__':
    
    
    process1 = multiprocessing.Process(target=print_number, args=(1, even_lock, odd_lock))
    process2 = multiprocessing.Process(target=print_number, args=(2, odd_lock, even_lock))
    
    process1.start()
    process2.start()

    process1.join()
    process2.join()

 
