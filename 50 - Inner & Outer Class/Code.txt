a = 50 #Global Variable
def abc():
    global a
    print(f"Print Statement 2 : {a}")
    a = 5 #Local Variable
    print(f"Print Statement 3 : {a}")

print(f"Print Statement 1 : {a}")
abc()
print(f"Print Statement 4 : {a}")