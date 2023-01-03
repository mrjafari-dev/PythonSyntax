#----------------------------------------------------------------------------------------------------------------
#Day 6 **********************************************************************************************************
#----------------------------------------------------------------------------------------------------------------


list = ['a','b','c','d','a']
#print true or false 
print('d' in list)
#print index of value in list
print(list.index('d'))
#print how many time accurs in our list 
print(list.count('a'))

#dictionary

dictionary = {
    'a':[1,2,3,4],
    'b':2,
    'c':3

}
print(dictionary['a'][3])

sampleList = [
   {
    'a':[1,2,3,4],
    'b':2,
    'c':3

},
    {
    'a':[5,6,7,8],
    'b':2,
    'c':3

}
]
print(sampleList[1]['a'][2])

print(dictionary.get('x',22))
user = dict(name = 'ali',family = 'rezayii')
print(user.get('name'))



