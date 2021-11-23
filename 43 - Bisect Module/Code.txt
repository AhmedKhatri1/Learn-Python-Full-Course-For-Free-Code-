#Bisect Module

import bisect

no = 5
my_list = [1,2,3,4,6,7,8,9,10]

print(my_list)
print(bisect.bisect(my_list,no))
bisect.insort(my_list,no)
print(my_list)

