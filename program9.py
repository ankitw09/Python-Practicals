b=int(input("Enter the number: "))
rev=0
temp=b
while temp!=0:
    digit=temp % 10
    rev=rev*10+digit
    temp=temp//10
if(rev==b):
    print("The Number ",b," is Palindrome")
else:
    print("The Number ",b," is Not Palindrome")