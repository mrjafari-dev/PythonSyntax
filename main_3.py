#----------------------------------------------------------------------------------------------------------------
#Day 3 **********************************************************************************************************
#----------------------------------------------------------------------------------------------------------------
selfish = 'abc'
selfish = selfish+'9'
print(selfish)
print(selfish[0:len(selfish)-2])
print(len(selfish))
print(selfish.upper())
print(selfish.capitalize())
print((selfish.find('c')))
print(selfish.replace('c', 'f'))


#birth_year = int(input('what year were you born?'))
#print(type(birth_year))
#year =2022 -  birth_year 
#print(f'your age is {year}')

#username = input('what is your username ? ')
#password = input('what is your password ? ')
#secretpass = '*' * len(password)

#print(f'{username} your pasword is  : {secretpass} is {len(secretpass)} letters long')


#lists
list = [0,"ali",1.5,True,4]
print(list[2])
#list Sliceing
amazonCard = [
    'noteBook',
    'sunglassess',
    'toys',
    'graphs',
]
amazonCard[2] = 'bnana'
# point to amazon card adress in memory
newCard = amazonCard
#copy amazon card valur in new card
newCard = amazonCard[:]
newCard[0] = 'ali'

print(newCard)
print(amazonCard)
#start in 27
