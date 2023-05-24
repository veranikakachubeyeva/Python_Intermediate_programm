# Write a function which takes one argument - the instance of any class. For any non-magic attribute which can be accessed via instance, 
#  create variable of the same name and pointing to the same value in global scope. 
# For example instance.attr value is 5, so "attr = 5" will be defined in global scope and can be accessed globally in module. Test your program 

def example4(obj):
        
    instance_non_magic_attrs_dir = [attr for attr in dir(obj) if not attr.startswith('__') and not attr.endswith('__')]       
         
    for item in instance_non_magic_attrs_dir:                 
            globals()[item] = getattr(obj, item)



class C:
    age = 1000000
    pass


class A(C):
    def fun_a():
        print("class a")
    def fun_a1():
        print("class a1")

a = A()

print(a.age)
print(a.__dict__)
a.nameA = "task4"
        
example4(a)

print(type(nameA))

print(f"global variable {nameA}")
print(f"global age {age}")


print(globals())
print((fun_a))

