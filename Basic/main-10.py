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



#while loop

i = 1
while i<50:
    print(i)
    i +=1
else :
    print("the end")


while True :
    respons = input('say something :')
    if respons == 'by':
        break


#Show Christmas Tee ^_^

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for items in picture:
    for value in items:
        if(value == 1):print('*',end='')
        else : print(' ',end = '')
    print('')


#start in 20 