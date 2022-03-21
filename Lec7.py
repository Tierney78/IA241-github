'''
Lec7
'''

def my_function(a,b):
    
    result = a+b
    
    return result
    
print(my_function(1,2))

def my_function(a,b=0):

    result = a+b
# a and b are parameters
# the default value of b is 0

    print('a is', a)    
    print('b is', b)

    return result

print(my_function(1))
print(my_function(b=2,a=1))

#ex1 cal abs values

def cal_abs(a):
    if a >=0:
        return a 
    if a < 0:
        return -a
print(cal_abs('b'))

#ex2
 
print('deez nuts')