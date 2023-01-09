#----------------------------------------------------------------------------------------------------------------
#Day 10 **********************************************************************************************************
#----------------------------------------------------------------------------------------------------------------

for item in 'mohammadreza' : print(item)

user = {
    'name':'reza',
    'family' : 'sds',
    'age' :22
}

for key , value  in user.items():
    print(key,value)


for index,item in enumerate('mohammadreza'):
    print(index,item)

#Enumerate work for strings tuples lists and sets

for index, value in enumerate({1,2,5,4}):
    print(index,value)


for key,items in enumerate(list(range(100))):
    if (key == 50):
        print(f"we in {key} keys in array")
    print(key,items) 



