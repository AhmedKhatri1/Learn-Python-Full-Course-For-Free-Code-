#Generator

#Example no 1:
# def list():
#     yield 1 #Yeild is that which will make your functiona generator
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#
# a = list()
# # print(a)
# # print(a.__next__())
# # print(a.__next__())
#
# for i in a:
#     print(i)

#Example no 2:

def list():
    l = 1

    while l<=10:
        square_root = l*l
        yield square_root
        l+=2

a = list()
for i in a:
    print(i)



