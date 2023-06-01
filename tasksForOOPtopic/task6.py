#- Write a class, instances of which works in the following way: 
#  obj.fun() # prints Hello! 
#  obj.aaaaa() # prints Hello! 
#  obj.any_name_you_imagine() # prints Hello! 
#  obj.__doc__ # all attributes starting with double underscore left untoched


class Task6:
    
    any_name_you_imagine = 100
    
    aaaa = 333  
    
    __abracadabra = 999
        
    def fun(self):       
        print ("Hello!")
        
    def __getattribute__(self, name):
        if not name.startswith('__') or not name.endswith('__'):        
            return object.__getattribute__(self, "fun")
        else:
            return object.__getattribute__(self, name)    
            
   
    
obj = Task6()
obj.b = 22

print(obj.__doc__)
print(obj.__dict__)


obj.fun()

obj.aaaa()

obj.bb__()

obj._b()

obj._b_()

obj.__b_()

obj.any_name_you_imagine()

obj.__abracadabra()
