#Lambda function
# def func(a):
#     return a + 5
#
# a = func(5)
# print(a)

#Function as an argument

func = lambda a : a + 5
sq = lambda x : x*x
sum = lambda a,b,c : a+b+c

a = 5
x = 3
a1 = 1
b = 2
c = 3

print(func(a))
print(sq(x))
print(sum(a1,b,c))
print(sum(a,1,2))

