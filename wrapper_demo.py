from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        print(func.__name__)
        result = func(*args)
        return result 
    
    return wrapper

@decorator
def add(a : int, b : int):
    return a+b

result = add(1,2)
print(result)
print("outside : ",add.__dict__)