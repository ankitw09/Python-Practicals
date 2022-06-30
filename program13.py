testtuple =int( input('Enter a value (enter exit to stop!): '))
mytuple = (testtuple,)


while True:
    
    if testtuple != -1:
       
        testtuple = int( input('Enter a value (enter exit to stop!): '))
       
        if testtuple != -1:
            
            mytuple = mytuple + (testtuple,)
    else:
        break

print(mytuple)
y = list(mytuple) # converting to list as tuple element we cant change

for i in range(0,len(y)):
    if y[i]%2==0:
        y[i] = 1
    else:
        y[i] = 0


mytuple=tuple(y)

print(mytuple)



