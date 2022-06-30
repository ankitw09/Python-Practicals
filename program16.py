#linear search 

def linear_search(arr, x):
    s=0
    while(s<len(arr)):
        if(arr[s]==x):
            return s
        s=s+1
    return -1





arr = []
n=int(input("enter no of element you want to insert"))
for i in range (0, n):
    ele=int(input())
    arr.append(ele)


arr.sort()
x= int(input("enter element you want to search in list: "))
result = linear_search(arr, x)

print(result)