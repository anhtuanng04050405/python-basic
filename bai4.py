def check(i, j):
    for _i in range (n):
        if x1[_i]<=i and y1[_i]<=j and i<=x2[_i] and j<=y2[_i]:
            return 1
        if x2[_i]<=i and y2[_i]<=j and i<=x1[_i] and j<=y1[_i]:
            return 1
    return 0

n = int(input())
ans=0

x1, y1, x2, y2 = [], [], [], []

for i in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)
for i in range (1, 101):
    for j in range (1, 101):
        ans=ans+check(i, j)

print(ans)