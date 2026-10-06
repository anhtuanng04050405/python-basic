n, q = map(int, input().split())
a = [0] + list(map(int, input().split()))
pre = [0]
for i in range(1, n + 1):
  pre.append(pre[-1] + a[i])
for _ in range(q):
  query = list(map(int, input().split()))
  loai = query[0]
  if loai == 1:
    x = query[1]
    a.append(x)
    pre.append(pre[-1] + x)
  elif loai == 2:
    a.pop()
    pre.pop()
  else:
    l, r = query[1], query[2]
    print(pre[r] - pre[l - 1])