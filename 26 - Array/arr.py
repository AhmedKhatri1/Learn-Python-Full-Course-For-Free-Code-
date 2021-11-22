#Array

# import array as arr
# # from array import *
# from array import arr

# array_1 = arr("i",[1,2,3,4,5])
import array as arr

array_1 = arr.array("i",[1,2,3,4,5])
# print(array_1)
# print(type(array_1))
# print(array_1[2])
# print(array_1)
# array_1.reverse()
# print(array_1)

array_2 = arr.array(array_1.typecode,(no*no*no for no in array_1))
# print(array_2)
# print(type(array_2))

# for i in range(len(array_1)):
#     print(array_1[i])
#
i = 0
while i<len(array_1):
    print(array_2[i])
    i+=1


