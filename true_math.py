from math import inf

def divide(first, second):
    if second ==0:
       print(inf)
    else:
        result = int(first/second)
        print(result)

divide(15,3)
divide(10,6)
divide(5, 0)