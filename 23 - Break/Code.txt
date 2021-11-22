#Break , continue, pass

stock = 10 #bat
a = int(input("Hello! Welcome to our shop!. How many bats you want to buy ?\n"))

i = 1
while i<=a:
    if i>stock:
        print("We only have 10 bats in stock!")
        break
    print("Bat")
    i+=1

print("Thanks for Shopping! Have a nice day. Good Bye!")
