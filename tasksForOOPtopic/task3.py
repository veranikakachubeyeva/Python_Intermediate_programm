#- Write a function which takes one argument - the instance of any class. Count number of all non-magic attributes, both in instance and in it's class. 
#  Return a tuple of those 2 numbers from function. Test your program 

def example3(obj):       
        
    instance_non_magic_attrs = [attr for attr in obj.__dict__ if not attr.startswith('__') and not attr.endswith('__')]
    class_non_magic_attrs = [attr for attr in obj.__class__.__dict__ if not attr.startswith('__') and not attr.endswith('__')]
       
    
    return len(instance_non_magic_attrs), len(class_non_magic_attrs)



class A:
    def fun_a():
        print("class a")
    def fun_a1():
        print("class a1")

class B(A):
    pass

a = A()
a.name = "task3"


b= B()  
      
print(example3(b))

print(example3(a))