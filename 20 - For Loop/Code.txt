#For Loop -- Looping

# # no = 2
# no = int(input("Enter a number to view multiplication table :"))
# for i in range(1,11):
#     print(no , 'x' , i, '=', no*i)

# my_list = ["Ahmed",10,"Ali",11]
# # print(my_list[0],my_list[1],my_list[2],my_list[3])
# for i in my_list:
#     print(i)

# my_list = [["Ahmed", 10], ["Ali", 11]]
# for i in my_list:
#     print(i)

# my_list = [["Ahmed", 10], ["Ali", 11]]
# print(type(my_list))
# dict = dict(my_list)
# print(dict)
# print(type(dict))

# my_list = [["Ahmed", 10], ["Ali", 11]]
# dict = dict(my_list)
#
# for i , a in dict.items():
#     print("Name is :",i,"and ID is :",a)

my_list = ["ahmed",1,2,3,5,10,99,108,9371,True,float]

for i in my_list:
    if str(i).isnumeric() and i>=10:
        print(i)
