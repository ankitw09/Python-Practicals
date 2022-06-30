# find prime between 1000 and 2000
testlist=[]
count =0
for i in range(1000, 2000):
    flag = 0
    for j in range (2, i//2):
        if i%j==0:
            flag = 1
    if(flag==0):
        print(i)
        count=count+1
        #testlist.append(i)

print(count)
#print(testlist)
