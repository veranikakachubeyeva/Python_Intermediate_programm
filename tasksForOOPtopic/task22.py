# - Write a function wich takes 2 arguments: arg1 and arg2 which are classes. For all methods which names start with 'fun_' swap them between classes 
# ( for example, method fun_1() in A should be moved to fun_1() in B and vice versa, etc). Test your program 


def example2(class1, class2):   
   
    class1_methods = {method: val for (method, val) in class1.__dict__.items() if method.startswith('fun_')}
    class2_methods = {method: val for (method, val) in class2.__dict__.items() if method.startswith('fun_')}
      
    
    def swap_attr(clsA, cls_meth, clsB):
        for method in cls_meth.keys():
            setattr(clsB, method, cls_meth[method])
            delattr(clsA, method)
        
    swap_attr(class1, class1_methods, class2)    
    swap_attr(class2, class2_methods, class1)
    
    return class2, class1
        
        
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