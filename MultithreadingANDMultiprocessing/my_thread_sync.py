import threading


lock = threading.Lock()

flag = 1

def func_print_even_numbers():
    global flag
    for num in range(2, 101, 2):        
        while not flag == 0:            
            pass
        lock.acquire()          
        print(num)
        flag = 1
        lock.release()
        
def func_print_odd_numbers():
    global flag
    for num in range(1, 100, 2):
        while not flag == 1:           
            pass
        lock.acquire()          
        print(num)
        flag = 0
        lock.release()

if __name__ == "__main__":
    
    t1 = threading.Thread(target=func_print_even_numbers)
    t2 = threading.Thread(target=func_print_odd_numbers)      
    
    t1.start()
    t2.start() 
    
    t1.join()  
    t2.join()     
    
