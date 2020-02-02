def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b:
        return a/b

def eva(string):    #1 + 2
    a,op,b = string.split()
    a,b=int(a),int(b)
    operations={
        "+":add,
        "-":sub,
        "*":mul,
        "/":div
    }
    operation=operations[op]
    return operation(a,b)