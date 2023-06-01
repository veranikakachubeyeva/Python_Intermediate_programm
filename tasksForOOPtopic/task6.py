#- Write a class, instances of which works in the following way: 
#  obj.fun() # prints Hello! 
#  obj.aaaaa() # prints Hello! 
#  obj.any_name_you_imagine() # prints Hello! 
#  obj.__doc__ # all attributes starting with double underscore left untoched


class Task6:
    """all attributes starting with double underscore left untoched"""
    any_name_you_imagine = 100
    
    aaaa = 333   
               
    
    def fun(self):       
        print ("Hello!")
        
    def __getattribute__(self, name):
        if name != "__doc__":
            return object.__getattribute__(self, "fun")
        else:
            return object.__getattribute__(self, "__doc__")
    
    
        
    
    
obj = Task6()


print(Task6.__doc__)

print(obj.__doc__)

obj.fun()

obj.aaaa()

obj.bb()

obj.any_name_you_imagine()