#Name: Abhijit Bag
#Regd No.: 2341002002
#PS Link: https://cses.fi/problemset/task/1094
n=int(input())
a=list(map(int,input().split()))
count=0
for i in range(1,n):
    d=a[i]-a[i-1]
    if d<0:
        count+=(-1*d)
        a[i]=a[i-1]
print(count)