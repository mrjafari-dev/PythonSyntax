#----------------------------------------------------------------------------------------------------------------
#Day 9 **********************************************************************************************************
#----------------------------------------------------------------------------------------------------------------
#loops
for item in [0,1,2,3,4,5,6] :
    for x in ['z','x','c'] :
        print(item, x)



user = {
    'name' : 'ali',
    'family' : 'rezayii',
    'age' : 26
}


for item in user:
    print(item)

print('-----------------------------')
    
for item in user.keys():
    print(item)

print('-----------------------------')

for item in user.values():
    print(item)

print('-----------------------------')

for key , value in user.items():
    print(key , value)

for item in range(0,100):
    print(item)

for item in range(10,20,3):
    print(item)


for item in range(10 ,0 ,-1):
    print(item)


for item in range(20):
    print(list(range(5)))
#start in 13
