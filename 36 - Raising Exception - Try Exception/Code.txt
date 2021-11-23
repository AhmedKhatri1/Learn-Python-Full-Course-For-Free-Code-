def add(no):
    try:
        return int(no) + 10
    except Exception as e:
        raise ValueError("Ye ghlt bt he yr, sahi int input kro!")

a = input()
b = add(a)
print(b)

