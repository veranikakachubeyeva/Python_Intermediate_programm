#- Write a class, instances of which works in the following way: 
#  obj.fun() # prints Hello! 
#  obj.aaaaa() # prints Hello! 
#  obj.any_name_you_imagine() # prints Hello! 
#  obj.__doc__ # all attributes starting with double underscore left untoched


class Task6():
    """all attributes starting with double underscore left untoched"""
    def fun(self):
        print ("Hello!")
        
    def __getattr__(self, name):
        return self.fun
        
    
    
obj = Task6()

print(obj.__doc__)

obj.fun()

obj.aaaa()

obj.any_name_you_imagine()