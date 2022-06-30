# implement a python program which read integer numbers from user and create a list.
# Then check every number in list is odd or even. Then replace odd numbers by 0 and even numbers by 1

list = []
n = int(input ("Enter the no of element want to insert in list"))
# inserting elements in list
for i in range (0,n):
    ele=int(input())
    list.append(ele)

# making odd numbers 0 and even 1 in list
for i in range(0,len(list)):
    if list[i]%2==0:
        list[i] = 1
    else:
        list[i] = 0

print(list)


