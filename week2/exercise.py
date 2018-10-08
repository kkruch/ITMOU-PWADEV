a=4
b=5

def f1(a,b,name=None):
    def perim(x,y):
        return 2*(x+y)

    def plosh(x,y):
        return x*y
    print(name)

    if name=='plosh':
        return plosh(a,b)
    if name=='perim':
        return perim(a,b)

print(f1(a,b,name='plosh'), f1(a,b,name='perim'))


"""
a = int(input())
b = int(input())

def f1(a,b,name=None):
    def perim(x,y):
        return 2*(x+y)

    def plosh(x,y):
        return x*y

    if name=='plosh':
        return plosh(a,b)
    if name=='perim':
        return perim(a,b)

print(f1(a,b,name='plosh'), f1(a,b,name='perim'))