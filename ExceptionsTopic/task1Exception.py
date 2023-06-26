#Write a dummy class decorator with keyword args (**kwargs). 
#  For each of key in kwargs get value (kwargs[key]):  if value is function create respective staticmethod in the decorated class with key name. 
#  For each string value, create respective class attribute (cls.key = kwargs[key]). 
#  For all other value types raise an Error. 
#  If the class already has a reachable attribute with such name, do not add attribute, but print a warning with module 'warnings' 


import warnings

def dummy_decorator(**kwargs):
    def decorator(cls):
        for key, value in kwargs.items():
            if callable(value):
                setattr(cls, key, staticmethod(value))
            elif isinstance(value, str):
                if hasattr(cls, key):
                    str_message = f"Attribute {key} already exists in class"
                    warnings.warn(str_message)
                else:
                    setattr(cls, key, value)
            else:
                raise ValueError(f"Invalid value type for key {key}")

        return cls
    return decorator


def class_method():
    print("class method was added to class")


@dummy_decorator(method1 = class_method, attribute2="val2", attribute1="val1")  #, attribute3 = 3)
class aClass:
   attribute1 = "val1" 


print(aClass.method1())

print(aClass.attribute1)

print(aClass.attribute2)





