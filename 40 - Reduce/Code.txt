#Reduce Function
from functools import reduce

sum = lambda a,b : a+b

my_list = [1,2,3,4,5]
a = reduce(sum,my_list)
print(a)
