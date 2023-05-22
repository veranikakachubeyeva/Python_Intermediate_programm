# Write a function which takes one argument - the instance of any class. For any non-magic attribute which can be accessed via instance, 
#  create variable of the same name and pointing to the same value in global scope. 
# For example instance.attr value is 5, so "attr = 5" will be defined in global scope and can be accessed globally in module. Test your program 

def example4(obj):
    instance_attrs = dir(obj)
    instance_non_magic_attrs = [attr for attr in instance_attrs if not attr.startswith('__') and not attr.endswith('__')]
    
    print(instance_non_magic_attrs)    
          
    for item in instance_non_magic_attrs:                 
            globals()[item] = getattr(obj, item)       


class A:
    def fun_a():
        print("class a")
    def fun_a1():
        print("class a1")


a = A()
a.name = "task4"
        
example4(a)

print(name)
print(globals())
print(fun_a)
print(fun_a1)