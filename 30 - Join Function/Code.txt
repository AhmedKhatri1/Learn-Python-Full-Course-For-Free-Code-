#Join Function

#Tuple
mobile = ("Apple","Huawei","Motorola")
a = '|'.join(mobile)
# print(a)

#List
tablet = ["Apple","Samsung","Lenovo"]
b = ','.join(tablet)
# print(b)

#Dictionary
Laptop = {
    'HP' : 10,
    'Lenovo' : 20,
    'Apple' : 30
}

d = ' and '.join(str(v) for v in Laptop.items())
c = ' and '.join(str(v) for v in Laptop.keys())
e = ' and '.join(str(v) for v in Laptop.values())

print(d)
print(c)
print(e)
