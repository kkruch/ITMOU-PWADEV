a=4
b=5

def f1(a,b):
    perim = lambda x,y: 2*(x+y)
    plosh = lambda x,y: x*y

    print(plosh(a,b), perim(a,b))

f1(a,b)

"""
a = int(input())
b = int(input())

def f1(a,b):
    perim = lambda x,y: 2*(x+y)
    plosh = lambda x,y: x*y

    print(plosh(a,b), perim(a,b))
    
f1(a,b)
"""