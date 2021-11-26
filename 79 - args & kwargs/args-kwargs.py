#args and kwargs -- they both are optional

print("--------------AGRS-------------") #send a list of value to a function
def args(no_list,*args):
    print(no_list)
    for i in args:
        print(i)

my_list = ["X","I","E","F"]
no_list = "125689"
args(no_list,*my_list)

print("--------------KWARGS-------------") #it sends a dictionary with values associate with keyword to a function

def kwargs(no_list,*args,**kwargs):
    print(no_list)

    for i in args:
        print(i)

    for y,z in kwargs.items():
        print(f"The name is :",y,"and the id is:",z)

my_list = ["X","I","E","F"]
my_list_2 = {"Ak":11,"Bk":12,"Ck":13}
no_list = "125689"

kwargs(no_list,*my_list,**my_list_2)


