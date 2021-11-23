try:
    a = int(input("Enter a number : "))

except Exception as e:
    print(e)
    exit()

finally: #it'll run rather error occur or not
    print("User input integer!")

print("Thanks for using the program!")