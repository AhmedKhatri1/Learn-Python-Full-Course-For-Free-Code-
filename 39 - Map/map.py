def sq(no):
    return no*no

my_list = [1,3,5]

a = list(map(sq,my_list))
b = list(map(lambda n : n*3,my_list))
print(a)
print(b)

