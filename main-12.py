#----------------------------------------------------------------------------------------------------------------
#Day 12 **********************************************************************************************************
#----------------------------------------------------------------------------------------------------------------

#set parameters for function 
def sum(num1,num2):
    return num1+num2


#call function and pass the argumants

print(sum(5,6))

#keyWord Arguments

print(sum(num2 = 2, num1=1))

#defualt value in function 
def say_helloo(name = "User124", emoji = "🥔"):
    print(f'hellooooo {name} {emoji}')

say_helloo('ali','🥔')



def test(num1,num2):

    def test2(n1,n2):
        return n1+n2

    return test2(num1,num2)
    #if i used return in function another line after return dont work 


toatl = test(1, 2)
print(toatl)


#methods vs function 

#functions :

#list()
#print()
#max
# or foexample i can creat function like sum()
# but methods is :
print("mohammadReza".find('R'))
# i called find from string and find is a method


def my_fun():
# docString :)
    '''
    Info : this function print somthing
    '''
    print('somthing')

print(my_fun.__doc__)


#start in 29
