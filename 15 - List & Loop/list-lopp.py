#Listing with loop

# for i in range(0,10):
#     print(i)

# no = int(input())
# for i in range(0,no):
#     print(i)

# list1 = ['itemno1','itemno2','itemno3']
# for i in list1:
#     print(i)

# list1 = ['itemno1','itemno2','itemno3']
# list2 = [[1,2,3],[4,5,6],[7,8,9]]
# for item in list2:
#     for i in item:
#         print(i)


#Creating an empty list
list = []

#number of elements as input
n = int(input("Enter number of elements : "))

#iterating till the range
for i in range(0,n):
    elements = int(input())
    list.append(elements) #adding the given elements to the list
print(list)
