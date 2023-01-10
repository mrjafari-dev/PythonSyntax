#----------------------------------------------------------------------------------------------------------------
#Day 4 **********************************************************************************************************
#----------------------------------------------------------------------------------------------------------------
# Matrix

matrix = [

[1,2,3,4],
['ali','mammad','reza']

]
print(matrix[1][2])

#adding in array 
list = [2,1,2,3,6,7]
newList = [6,2,2,2,2]
list.insert(6, 100)
list.append(5)
list.extend(newList)
print(list)
print(newList)

#removing

#remove item with value
list.remove(2)

#remove item with index
list.pop(4)

#remove All item of array
list.clear()
print(list)
