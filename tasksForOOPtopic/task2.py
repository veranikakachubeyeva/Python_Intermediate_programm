# - Write a function wich takes 2 arguments: arg1 and arg2 which are classes. For all methods which names start with 'fun_' swap them between classes 
# ( for example, method fun_1() in A should be moved to fun_1() in B and vice versa, etc). Test your program 


def example2(class1, class2):    
    methods1 = [method for method in class1.__dict__ if method.startswith('fun_')]    
    methods2 = [method for method in class2.__dict__ if method.startswith('fun_')]    
    
    
    def del_attr(meth, cls): 
        method_value = []
        for meth in meth:
            method_value.append(getattr(cls, meth))
            delattr(cls, meth)     
        return method_value
    
    method1_value = del_attr(methods1, class1) 
    method2_value = del_attr(methods2, class2)
       
      
    def set_attr(meth, meth_val, cls):
        for el in meth:
            for val in meth_val:
                setattr(cls, el, val)
        
    set_attr(methods1, method1_value, class2)
    set_attr(methods2, method2_value, class1)
     
    
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
        
class C(A):
    pass
        

#example2(A, B)

example2(C, B) 

print("dir C")
print(dir(C))

print("dict C") 
print(C.__dict__)

print("dir B")
print(dir(B)) 

print("dict B") 
print(B.__dict__)



print("dir A")
print(dir(A))       

print("dir B")
print(dir(B))  

#print(A.fun_b)     