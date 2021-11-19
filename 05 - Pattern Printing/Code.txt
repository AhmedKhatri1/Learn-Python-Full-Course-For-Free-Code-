#Pattern printing

# print("# ",end='')
# print("# ")
# print("# ",end='')
# print("# ")

# for i in range(5):
#     for j in range(5):
#         print("* ",end="")
#     print()

#For printing using for loop
#
##
###
####
#####

# for i in range(5):
#     for j in range(i+1):
#         print("* ",end="")
#     print()
#
# for i in range(5):
#     for j in range(5-i):
#         print("* ",end="")
#     print()

#Diamond Pattern

p = 9
for a in range(1,(p+1)//2+1):
    for b in range((p+1)//2 - a):
        print(" ",end="")
    for c in range((a*2)-1):
        print("*",end="")
    print()

for a in range((p+1)//2 + 1, p + 1):
    for b in range(a - (p+1)//2):
        print(" ",end="")
    for c in range((p+1 -a)*2 -1):
        print("*",end="")
    print()