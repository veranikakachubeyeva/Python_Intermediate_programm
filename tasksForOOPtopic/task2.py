# - Write a function wich takes 2 arguments: arg1 and arg2 which are classes. For all methods which names start with 'fun_' swap them between classes 
# ( for example, method fun_1() in A should be moved to fun_1() in B and vice versa, etc). Test your program 


def example2(class1, class2):
    methods1 = [method for method in dir(class1) if method.startswith('fun_')]
    method1_value = []    
    for meth in dir(class1):
        if meth.startswith('fun_'):
            method1_value.append(getattr(class1, meth))
            delattr(class1, meth)
    print(method1_value)
    print(methods1)
     
        
    methods2 = [method for method in dir(class2) if method.startswith('fun_')]
    method2_value = []     
    for meth in dir(class2):
        if meth.startswith('fun_'):
            method2_value.append(getattr(class2, meth))
            delattr(class2, meth)
    print(method2_value)
    print(methods2)    
    
         
    for el in methods1:
        for val in method1_value:
            setattr(class2, el, val)
        
    for el in methods2:
        for val in method2_value:
            setattr(class1, el, val)
     
    
    return class1, class2
        
        
class A:
    def fun_a():
        print("class a")
    def fun_a1():
        print("class a1")        


class B:
    def fun_b():
        print("class b")
    def fun_b1():
        print("class b1")
        
example2(A, B) 


print(dir(A))       

print(dir(B))  

print(A.fun_b)     