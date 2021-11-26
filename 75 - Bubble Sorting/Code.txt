#Bubble Sort

def bubble_sorting(my_list):
    n = len(my_list)

    for i in range(n-1):
        for j in range(0,n-i-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1]=my_list[j+1],my_list[j]

print("Before sorting")
my_list = [1,2,5,6,11,8,3,90,4,76,99]
for i in my_list:
    print(i)
print((my_list))

print("After sorting")
bubble_sorting(my_list)
for i in range(len(my_list)):
    print("%d"%my_list[i])

