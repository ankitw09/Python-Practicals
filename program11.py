list1=[]
n=int(input("Enter no of elements in list:  "))
for i in range(0,n):
    ele=int(input())
    list1.append(ele)

neg_ele=0
pos_ele=0

for i in range(0 , n):
    if list1[i] < 0:
        neg_ele=neg_ele+1
    else:
        pos_ele=pos_ele+1

print(list1)

list1.clear()

list1=[{'N':neg_ele , 'P':pos_ele}]
print("list after adding")
print(list1)
