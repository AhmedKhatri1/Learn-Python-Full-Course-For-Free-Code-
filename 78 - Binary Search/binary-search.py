#binary search
#all the values in the list must be sorted!!!

def binary_search(my_list,a,y,z):
    while y <= z:
        x = y + (z-y)//2
        if my_list[x] == a:
            return x
        elif my_list[x] < a:
            y = x + 1
        else:
            z = x - 1
    return -1

my_list = [5,7,9,13,19,25,28,1010,2197]
a = 1010

final_res = binary_search(my_list,a,0,len(my_list)-1)

if final_res != -1:
    print("Your number is found at index no :",str(final_res))
else:
    print("Tata! Bye Bye! Khatam!")