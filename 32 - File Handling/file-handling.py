#File handling

# file_1 = open("ak.txt","wb")
# print(file_1.name)
# print(file_1.mode)
# file_1.write(bytes("Hello! Here Ahmed!","UTF-8"))
# file_1.close()

a = open("ahmed.txt","rt")
print(a.readline()) #For normal printing
print(a.readlines()) # For printing in list format

# b = a.read()

# for i in a:
#     print(i)
# print(b)
a.close()
