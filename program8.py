# merge 2 list in sorted order and remove duplicate

list1=[10,20,35,35,21,46,99,84,15,26]
list2=[30,20,25,41,21,99,85,23,12,36]

list3=sorted(list1+list2)

list4=[]

for i in list3:
    if i not in list4:
        list4.append(i)


print(list4)

