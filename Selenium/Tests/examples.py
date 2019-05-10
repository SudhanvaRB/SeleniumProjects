'''
Created on Dec 27, 2018

@author: subharad
'''
from _ast import Num

def check_prime(input_no):
    if input_no > 1 :
        for i in range(2,input_no):
            if (input_no % i) == 0:
                print("number is not prime")
                break
        else:
            print("number is prime")
            
    else:
        print("number is prime")
        
check_prime(2)


def factorial(input_no):
    res = 1
    for i in range(1,input_no+1):
        res = res * i
    print(res)

factorial(6)

num = 1

while num < 10:
    print(num)
    num = num + 9
    

        
def tables(num):
    for i in range(1,11):
        print(str(num) + "X" + str(i) + "=" + str((num * i)))
        
tables(6)

listno = [1 , 2 , 3 , 4]
listno[2] = -75
print(listno)

#===============================================================================
# exe = [1, 2, 3, 4, 5]
# nl =exe[:len(exe)-1]
# if 9 in nl:
#     print("True")
# else:
#     print("false")
#     
#===============================================================================
def array_front9(nums):
    nl =nums[:len(nums)-1]
    if 9 in nl:
        return True
    else:
        return False
        
array_front9([1, 2, 9, 3, 4])


items = [1,1,1,4,4]

stats = {}
for i in items:
    if i in stats:
        stats[i] += 1
    else:
        stats[i] = 1

print(stats)

my_list = [4, 7, 0, 3]

my_iter = my_list.__iter__()

#print(my_iter)
print(my_iter.__next__())
print(my_iter.__next__())


def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
    
def gen():
    n=1
    while n < 5:
        yield n
        n+=1
b = gen()

    
    
    
a = my_gen()
print(next(a))

print(a.__next__())

def inc(x):
    return x + 1
    
def cal(fun,x):
    result = fun(x)
    return result
print(cal(inc,5))


def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))

foo("Hi")


    

   

      
  
    
    
        