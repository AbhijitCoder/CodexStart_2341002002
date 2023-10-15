#Name: Abhijit Bag
#Regd No.: 2341002002
#PS Link: https://cses.fi/problemset/task/1069
S= input()
count=1
max=1
for i in range(1,len(S)):
    if S[i]==S[i-1]:
        count+=1
    else:
        count=1
    if count>max:
        max=count
print(max)