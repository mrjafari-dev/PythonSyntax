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
print(1 in dictionary.items())

#copy value of user in another of ram adress
user2= user.copy()
#add value to dictionary
user2.update({'age':22})
#remove end value 
user2.popitem()
#Remove value
user2.pop('name')
print(user2)

#tuples like to arrays but inmutable 

tpl = (0,1,2,3)
print(tpl)

#set in phyton remove duplicate values 

setValue = {1,2,3,4,5,6,6,6,}
testList=[1,2,3,4,5,5,5,5]
print(setValue)
print(set(testList))
