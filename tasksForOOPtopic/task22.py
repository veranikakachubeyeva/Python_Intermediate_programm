# - Write a function wich takes 2 arguments: arg1 and arg2 which are classes. For all methods which names start with 'fun_' swap them between classes 
# ( for example, method fun_1() in A should be moved to fun_1() in B and vice versa, etc). Test your program 


def example2(class1, class2):   
   
    class1_methods = {method : val for (method, val) in class1.__dict__.items() if method.startswith('fun_') and callable(val)}
    class2_methods = {method: val for (method, val) in class2.__dict__.items() if method.startswith('fun_') and callable(val)}
    
       
    #def swap_attr(clsA, cls_meth, clsB):
        #for method in cls_meth.keys():
            #setattr(clsB, method, cls_meth[method])
            #delattr(clsA, method)
        
    #swap_attr(class1, class1_methods, class2)    
    #swap_attr(class2, class2_methods, class1)
    
    for method in class1_methods.keys():
        setattr(class2, method, class1_methods[method])
        delattr(class1, method)
    for method in class2_methods.keys():
        setattr(class1, method, class2_methods[method])
        delattr(class2, method)

    
    return class2, class1
        
        
class A:
    fun_attr = 100
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
        

example2(A, B) 

   
assert hasattr(A, "fun_attr"), "fun_attr was  moved from class A to class B"
assert hasattr(A, "fun_b"), "fun_b was not moved from class B to class A"
assert hasattr(A, "fun_b1"), "fun_b1 was not moved from class B to class A"

assert not hasattr(B, "fun_attr"), "class B has fun_attr from class A"
assert hasattr(B, "fun_a"), "fun_a was not moved from class A to class B"
assert hasattr(B, "fun_a1"), "fun_a1 was not moved from class A to class B"