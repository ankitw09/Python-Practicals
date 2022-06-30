# implement a python program which read integer numbers form user and create a tuple.
# Then check every number in tuple is negative or positive and replace negative no by 0 and postive no by 1

testtuple =int( input('Enter a value (enter -1 to stop!): '))
mytuple = (testtuple,)


while True:
    
    if testtuple != -1:
       
        testtuple = int( input('Enter a value (enter -1 to stop): '))
       
        if testtuple != -1:
            
            mytuple = mytuple + (testtuple,)
    else:
        break


print(mytuple)
y = list(mytuple) # converting to list as tuple element we cant change

for i in range(0,len(y)):
    if y[i] < 0:
        y[i] = 0
    else:
        y[i] = 1


mytuple=tuple(y)

print(mytuple)