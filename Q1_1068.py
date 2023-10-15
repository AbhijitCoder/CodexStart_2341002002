#Name: Abhijit Bag
#Reg No.: 2341002002
#PS Link: https://cses.fi/problemset/task/1069
 
N = int(input())
print(N, end=" ")
while N>1:
    if N%2==0:
        N=N//2
    else:
        N=(N*3)+1
    print(N, end=" ")