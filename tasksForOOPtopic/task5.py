#OOP Task 5

#Create class Number with weight attribute (int). Number class has 2 methiods only: __ init __ (assigns initial value to attribute) 
# and __ add __ . 
#  The last method __ add __ must work only with args of int type, the others should result in returning 
# "TypeError: unsupported operand type(s)" as builtin int does. __add __ return type: int (weight + other:int). 
#  Create similar class NumberBrother, with only 2 methods __ init__ and __ radd__. 
# The __ init __ is the same as above, while __ radd __ must support the following expression: 
#>>> Number(10) + NumberBrother(20) (return 30 of type int) 
#  At the end, those test must pass: 
#>>> Number(10) + 50 
#>>> Number(10) + NumberBrother(20) 
#  Those should raise TypeError: 
#>>> Number(10) + 55.55 
#>>> 111 + Number(10) 
#>>> NumberBrother(20) + Number(10) 


class Number:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        if isinstance(other, int):
            return self.val + other
        else: 
            return NotImplemented
                
          

class NumberBrother:
      def __init__(self, val):
        self.val = val
        
      def __radd__(self, other):
        return self.val + other.val
       

print(Number(50) + 10)

print(Number(50) + NumberBrother(20))

#print(Number(10) + 55.55)

#print(111 + Number(10))

print(NumberBrother(20) + Number(10))