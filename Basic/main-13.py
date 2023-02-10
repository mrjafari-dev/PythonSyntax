#----------------------------------------------------------------------------------------------------------------
#Day 13 **********************************************************************************************************
#----------------------------------------------------------------------------------------------------------------
 
# *args 

def superFunction(*args):
    print(args)
    print(*args)
    print(sum(args))

def kwargsFunction (**kwargs):
    print(kwargs)
    for item in kwargs.values():
        print(item)


superFunction(1,2,3,4,5,6)
kwargsFunction(name ='ali',family = 'reza',age =21)



def loopFun(list):
    for item in list:
        if(item%2==0):
            #if run return breack lopp and exite from functions
            return item


print(loopFun(list =[1,3,3,4,5,6]))

name = "mohammadreza"

if len(name)>5:
    print(f"yor name  is have {len(name)} char")


if (n := len(name))>5:
    print(f"yor name  is have {n} char")




#Scope in python 
#global 

age = 10 

def count():
    global age 
    age += 2
    return age


count()
count()
print(count())


#nonelocal 
x = "global"
def outer():
    x="local"
    def inner():
        nonlocal x 
        x = "nonLocal"
        print(f"inner : {x}")
        
    inner()
    print(f"outer : {x}")

outer()


