#----------------------------------------------------------------------------------------------------------------
#Day 11 **********************************************************************************************************
#----------------------------------------------------------------------------------------------------------------

#how to remove dupliate value in list
mylist = ['a','b','c','a','f','b']
some_list = set(mylist)
print("with SET : ",list(some_list))

duplicate =[]
for x in mylist:
   if mylist.count(x)>1:
        duplicate.append(x)
        mylist.remove(x)

print(duplicate)
print("with LOOP : ",mylist)

#funcation in python

def helloWorld():
    print("hello World")

helloWorld()

def say_helloo(name , emoji):
    print(f'helllooooo{name}{emoji}')


say_helloo("moahhamdreza", "🥰")