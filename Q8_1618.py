#Name: Abhijit Bag
#Regd No.: 2341002002
#PS Link: https://cses.fi/problemset/task/1618
N = int(input())
c = 0
i = 5
while(N/i>= 1):
    c += int(N/i)
    i *= 5

print(c)