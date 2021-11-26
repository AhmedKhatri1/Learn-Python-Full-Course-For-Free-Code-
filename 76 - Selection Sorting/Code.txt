#selection sort

import sys

my_list = [1,2,5,6,11,8,3,90,4,76,99]
print("Before sorting")
print(my_list)
for i in range(len(my_list)):
    min_index = i
    for j in range(i+1,len((my_list))):
        if my_list[min_index] > my_list[j]:
            min_index = j
    my_list[i], my_list[min_index]= my_list[min_index],my_list[i]

print("After sorting")
for i in range(len((my_list))):
    print("%d"%my_list[i])

