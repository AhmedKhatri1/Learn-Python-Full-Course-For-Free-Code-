#format function

first_name = "Ahmed"
last_name = "Khatri"
teaching = "Python"

a = "This is me : {} {} and I'm teaching you : {}".format(first_name,last_name,teaching)
print(a)
b = "This is me : {2} {1} and I'm teaching you : {0}".format(first_name,last_name,teaching)
print(b)
c = "This is me : {0} {0} and I'm teaching you : {0}".format(first_name,last_name,teaching)
print(c)


