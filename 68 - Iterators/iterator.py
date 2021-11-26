#iterators

my_list = [1,2,3,4,5]

# print(my_list[0])
# for i in my_list:
#     print(i)

my_iterator = iter(my_list)
#
# print(my_iterator.__next__())
# print(my_iterator.__next__())
# print(my_iterator.__next__())
# print(my_iterator.__next__())
# print(my_iterator.__next__())
#
# for i in my_iterator:
#     print(i)

print(my_iterator.__next__())
print(next(my_iterator))




