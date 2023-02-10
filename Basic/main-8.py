#----------------------------------------------------------------------------------------------------------------
#Day 8 **********************************************************************************************************
#----------------------------------------------------------------------------------------------------------------

#truthy and falsy
print(bool(''))
print(bool(0))
print(bool('mohammad'))
print(bool(1))

username = 'alireza'
password = '1234'
if username and password :
    print('you can login')

con = bool (int(input("enter  1 for true and 0 to false ")))

message = "true message " if con else "false message"

print(message)

print(not(True))

print('1' is '1')
print('1' == '1')

c = 'ali'
g = 'ali'
print(c is g)

#loops 

for item in [0,1,2,3,6]:
    for x in {'x','d','w'} :
     print(item,x)

     #Start in 11