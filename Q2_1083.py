#Name: Abhijit Bag
#Reg No.: 2341002002
#PS Link: https://cses.fi/problemset/task/1083
N= int(input())
a = list(map(int,input().split()))
print(N*(N+1)//2 - sum(a))