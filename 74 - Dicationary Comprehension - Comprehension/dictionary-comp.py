#dictionary comprehension

#keys and values
# dict_1 = {}
# for i in range(5):
#     dict_1[i] = i*2
# print(dict_1)
#
# dict_2 = {i:i*3 for i in range(5)}
# print(dict_2)

# dict_1 = {}
# for i in range(5):
#     if i%2==0:
#         dict_1[i]= i*2
#     else:
#         dict_1[i]= "It is not divisible by 2. so sorry sir"
# print(dict_1)
#
# dict_2 = {i:(i if i%2==0 else 'Invalid Sir!') for i in range(5)}
# print(dict_2)

#List & Dictionary Together
my_list = [(1,"A"),(2,"B")]
dict_1 = {a:b for a,b in my_list}
print(my_list)
print(dict_1)
