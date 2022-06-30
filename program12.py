#Program for selection sort
list1=[]
n = int(input("Enter No of elements: "))
# inputing elements in list
for i in range(0, n):
    ele=int(input())
    list1.append(ele)

# selection sort in python
for i in range(0, n-1):
    min = i
    for j in range (i+1, n):
        if list1[min] > list1[j]:
            min=j
    #swapping logic
    list1[min],list1[i]=list1[i],list1[min]
   
# printing the sorted list
print(list1)

