def divide(a,b):
    if b==0:
        raise ValueError("Divion by zero is not allowed")
    return a/b
divide(2,0)