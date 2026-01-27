def display_decorator(myFunction):

    def wrapper(*args, **kwargs):
        print("Working in wrapper ............")
        myFunction(*args, **kwargs)
        print("Working in wrapper ............")
        
    return wrapper

@display_decorator
def myFunction(a,b):
    print(f"Working in myFunction.. value of a: {a} and b: {b} ")

myFunction(5,4)