#- Write a class which creates obj. Class must implement: 
#a) __getattribute__ checks if attr name  == "hello" -> return "hello world" else -> default behavior 
#b) __getattr__ checks if attr name  == "love" -> return "love you" else -> return None 
#c) __setattr__ checks if attr name  == "vasia" -> assign obj.name = "pupkin" else -> assign obj.name = value 
#d) write test to prove if everything works 


class Example1:
    
    def __getattribute__(self, attrname):
        if attrname == 'hello':
            return 'hello world'
        else:
            return object.__getattribute__(self, attrname)
                 
    def __getattr__(self, attrname):
        if attrname == "love":
            return print("love you")
        else:
            return None
        
    def __setattr__(self, attrname, value):
        if attrname == 'name':            
            self.__dict__[attrname] = "pupkin"
        else:            
            self.__dict__[attrname] = value
        
        
obj = Example1()

print(obj.hello)
obj.hello = "HELLO"
print(obj.hello)
print("//////////////////////////////////////")


print(obj.love)
obj.love = "LoVE"
print(obj.love)
print("//////////////////////////////////////")


print(obj.name)
obj.name = "NAME"
print(obj.name)
