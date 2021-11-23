#Filter

def greater(no):
    if no > 2:
        return True
    else:
        return False

grtr_5 = lambda no : no > 5

my_list = [1,2,3,4,5,10,20,25,45,100]
print(list(filter(greater,my_list)))
print(list(filter(grtr_5,my_list)))

