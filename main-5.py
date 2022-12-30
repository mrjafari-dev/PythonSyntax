#----------------------------------------------------------------------------------------------------------------
#Day 5 **********************************************************************************************************
#----------------------------------------------------------------------------------------------------------------

list = ['c','b','a','f','e','d']
#how to  find index of value 
#index(value,strtIndex,endIndex)

print(list.index('b',0,len(list)))

#index return index of item but "in" return true or false 
print('e' in list)

print(list.count('t'))
#Sort List
newList = list[:]
list.sort()
print(list)
print(sorted(newList))

list.reverse()
print(list)
print(list[0::-1])
print(list)

test = ' '
#return value to newTest 
newTest = test.join(['my','name','is','mohammadreza'])
print(test)
print(newTest)