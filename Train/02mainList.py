list = ['ali',0,'a',1,2,3]
print(list[0])
list[1]="mohammareza"
print(list)
matrix=[
    ['a','b'],
    [1,2,3]
]
print(matrix)
matrix[0][1]='c'
print(matrix)

#add 
list.insert(6,4)
list.append("ali")
list.extend([1,2,3,4])
print(list)

#remove
list.remove('ali')
list.pop(6)
print(list)


list.clear()
print(list)