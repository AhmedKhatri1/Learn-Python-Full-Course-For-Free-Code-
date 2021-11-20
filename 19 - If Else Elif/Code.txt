#If else elif

print("Welcome to Parent's Teacher Meeting!")
print("Enter student's marks : ")
no = int(input())

if (no>=91 and no<=100):
    a = print("Grade A")
elif (no>=81 and no<=90):
    a = print("Grade B")
elif (no>=71 and no<=80):
    a = print("Grade C")
elif (no>=61 and no<=70):
    a = print("Grade D")
elif (no>100):
    a = print("System Error!")
elif (no==60):
    a = print("Student just pass!")
else:
    print("Student Failed!")

print("Thanks for joining today's meeting!")