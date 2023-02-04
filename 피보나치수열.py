#! /bin/python3 python3
from distutils.log import debug


num = 1
prev = 0
cur = 1
while num < 10:
    next = cur + prev
    print ('%2d %d' % (num, next))
    prev = cur
    cur = next
    num += 1
for i in [0,1,2,3,4,5]:
    if i % 2 != 0:
        continue
    print('%d ^ 2 = %d' %(i, i*i))

def counter(max):
    t = 0
    def output():
        print('t=%d' %t)
    while t < max:
        output()
        t += 1
counter(10)

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))

def divide (a,b):
    return(a/b, a%b)
q, r = divide(3,2)
print(q,r)

a = lambda x, y : x+y
b = a(1, 2)
print (b)

def func(f):
    return f()

def hello():
    return "Hello World"

print (func(hello))

def counter2(first):
    t = [first]
    def increment():
        t[0] += 1
        return t[0]
    return increment

timer = counter2(5)

print (timer())
print (timer())

@debug
def incr(x):
    return x+1

def incr(x):
    return x + 1
incr = debug(incr)


