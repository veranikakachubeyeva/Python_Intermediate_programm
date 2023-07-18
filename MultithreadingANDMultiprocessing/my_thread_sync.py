import threading

lock = threading.Lock()

current_number = 1

def func_print_even_numbers():
    global current_number
    while current_number <= 99:
        with lock:
            if current_number % 2 == 0:
                print(current_number)
                current_number += 1
        
def func_print_odd_numbers():
    global current_number
    while current_number <= 99:
        lock.acquire()
        try:
            if current_number % 2 == 1:
                print(current_number)
                current_number += 1
        finally:
            lock.release()

if __name__ == "__main__":
    
    t1 = threading.Thread(target=func_print_even_numbers)
    t2 = threading.Thread(target=func_print_odd_numbers)      
    
    t1.start()
    t2.start() 
    
    t1.join()  
    t2.join()     
    
