#python code to find no divisible by 7 but not by 5
list1=[]
count = 0
for x in range(2000, 3200):
    if (x%7==0) and (x%5!=0):
        list1.append(str(x))
        count=count+1

        
print (','.join(list1))
print(count)
