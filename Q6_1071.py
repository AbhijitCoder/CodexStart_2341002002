#Name: Abhijit Bag
#Regd No.: 2341002002
#PS Link: https://cses.fi/problemset/task/1071
t = int(input())

for i in range(t):
    y, x = map(int, input().split())

    if y > x:
        if y % 2:
            ans = (y - 1) ** 2 + x
        else:
            ans = y ** 2 - x + 1
    else:
        if x % 2:
            ans = x ** 2 - y + 1
        else:
            ans = (x - 1) ** 2 + y

    print(ans)