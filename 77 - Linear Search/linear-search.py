#linear search

def linear_search(my_list,n,a):
    for i in range(0,n):
        if my_list[i] == a:
            return i
    return -1

my_list = [5,1,9,4,0,2,7]
a = 9
n = len(my_list)

final_res = linear_search(my_list,n,a)
if final_res == -1:
    print("Your number is not found!")
else:
    print("Your number is found at :",final_res)
