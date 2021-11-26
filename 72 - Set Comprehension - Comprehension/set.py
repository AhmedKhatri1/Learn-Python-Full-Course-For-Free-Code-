#set comprehension

a = [1,2,3,4,5,66,77,99,10,12,16,20,86]
b = [i for i in a if i%2==0]
print(b)

my_list = [1,3,5,2,2,1,2,3,8,5,4,4,1]
set = {i for i in my_list}
print(set)