#list comprehension

#This is normal way
# a = [1,1,2,2,6,6,5,3,4,8,4,8,6,9,90,10,86,81,74,98]
# b = []
#
# for i in a:
#     if i%2==0:
#         b.append(i)
# print(b)

#shorcut way to create a new list

a = [1,1,2,2,6,6,5,3,4,8,4,8,6,9,90,10,86,81,74,98]
b = [i for i in a if i%2==0]
print(b)
print(len(b))
