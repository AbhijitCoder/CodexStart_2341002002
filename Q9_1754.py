#Name: Abhijit Bag
#Regd No.: 2341002002
#PS Link: https://cses.fi/problemset/task/1754

t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    if a < b:
        a, b = b, a

    if a > 2 * b:
        print("NO")

    
    elif (a + b) % 3 == 0:
        print("YES")
    else:
        print("NO")