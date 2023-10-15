#Name: Abhijit Bag
#Regd No.: 2341002002
#PS Link: https://cses.fi/problemset/task/1623
N = int(input())
W = list(map(int, input().split()))
def min_difference(index, a, b):

    if index >= len(W):
        return abs(a - b)

    return min(min_difference(index + 1, a + W[index], b), min_difference(index + 1, a, b + W[index]))

print(min_difference(0, 0, 0))