# Try exception

print("Welcome!")

while True:
    print("Press q to exit!")
    a = input("Enter a number : ")
    if a == 'q':
        break
    try:
        a = int(a)
        if a > 10:
            print("You entered a number which is greater than 10")
    except Exception as e:
        print("Your input resulted in an error")
        # print(f"Your input resulted in an error {e}")

print("Thanks for playing!")