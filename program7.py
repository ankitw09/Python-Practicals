
#Prime number program
a = int(input())
flag = 0
for i in range (2,a//2):
    if a%i==0:
        flag=1

if flag == 1:
    print("Number is Not Prime : ")
else:
    print("Number is  Prime")
