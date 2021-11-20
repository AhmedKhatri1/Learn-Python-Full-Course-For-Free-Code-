#Tuples and list together

user = input("Enter numbers using separated commas : ")
my_list = user.split(",")
my_tuple = tuple(my_list)
print("Your list is :",my_list)
print(type(my_list))
print("Your tuple is :",my_tuple)
print(type(my_tuple))
