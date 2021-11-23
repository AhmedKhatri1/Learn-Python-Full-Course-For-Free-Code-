# Recursion -- calling a function by itself
# Factorial -- 5! = 5x4x3x2x1 = 120, 4! = 4x3x2x1 = 24, 0!

def function(a):
    if a == 0:
        return 1
    return a * function(a - 1)  # calling a function by itself

print("Enter a number for which you want a factorial : ")
b = int(input())
c = function(b)
print("The factorial of number {} is : {}".format(b, c))
