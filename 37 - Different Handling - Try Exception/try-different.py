try:
    a = int(input("Enter a number :"))
    b = int(100/a)
    print(b)
except ValueError as e:
    print("Please enter a valid value!")
except ZeroDivisionError as e:
    print("Hey, You sure you don't put a zero (0) value ?")
