#- Write a function which takes one argument - the instance of any class. Count number of all non-magic attributes, both in instance and in it's class. 
#  Return a tuple of those 2 numbers from function. Test your program 

def example3(obj):
        
    instance_attrs = dir(obj)
    class_attrs = dir(obj.__class__)
    
    instance_non_magic_attrs = [attr for attr in instance_attrs if not attr.startswith('__') and not attr.endswith('__')]
    class_non_magic_attrs = [attr for attr in class_attrs if not attr.startswith('__') and not attr.endswith('__')]
    
    conter_obj_attrs = len(instance_non_magic_attrs)
    conter_class_attrs = len(class_non_magic_attrs)
    
    return print((conter_obj_attrs, conter_class_attrs))


class A:
    def fun_a():
        print("class a")
    def fun_a1():
        print("class a1")

a = A()
a.name = "task3"
        
example3(a)