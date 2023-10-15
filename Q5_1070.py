#Name: Abhijit Bag
#Regd No.: 2341002002
#PS Link: https://cses.fi/problemset/task/1070
N=int(input())
if N==1:
    print("1")
elif N<=3:
    print("NO SOLUTION")
else:
    for i in range(2,N+1,2):
        print(i,end=" ")
    for i in range(1,N+1,2):
        print(i,end=" ")
