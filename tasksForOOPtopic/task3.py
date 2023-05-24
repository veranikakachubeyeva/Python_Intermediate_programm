#- Write a function which takes one argument - the instance of any class. Count number of all non-magic attributes, both in instance and in it's class. 
#  Return a tuple of those 2 numbers from function. Test your program 

def example3(obj):       
        
    instance_non_magic_attrs = [attr for attr in obj.__dict__ if not attr.startswith('__') and not attr.endswith('__')]
    class_non_magic_attrs = [attr for attr in obj.__class__.__dict__ if not attr.startswith('__') and not attr.endswith('__')]
       
    
    return len(instance_non_magic_attrs),  len(class_non_magic_attrs)



class A:
    def fun_a():
        print("class a")
    def fun_a1():
        print("class a1")

class B(A):
    pass

a = A()
a.name = "task3"


b = B()  


assert example3(b) and isinstance(example3(b), tuple), \
    f"result is not a tuple: {example3(b)}"

assert example3(a) and isinstance(example3(a), tuple), \
    f"result is not a tuple: {example3(a)}"   
    
assert example3(b) and example3(a)[0]>=0 and example3(a)[1]>=0, \
    f"result is less than 0, expected : {example3(a)}"

assert example3(b) and example3(b)[0]>=0 and example3(b)[1]>=0, \
    f"result is less than 0, expected : {example3(b)}" 
    
assert example3(b) and example3(a)[0]<0 and example3(a)[1]<0, \
    f"result is not ok, expected : {example3(a)}"

assert example3(b) and example3(b)[0]<0 and example3(b)[1]<0, \
    f"result is not ok, expected : {example3(b)}"

     
#print(example3(b))

#print(example3(a))