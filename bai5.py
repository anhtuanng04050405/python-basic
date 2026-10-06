n, q = map(int, input().split())
arr = list(map(int, input().split()))

def solve0(val):
    arr.append(val)

def solve1(i, val):
    arr[i - 1] = val

def solve2(l, r):
    arr[l - 1:r] = sorted(arr[l - 1:r])

def solve3():
    print(*arr)

for _ in range(q):
    data = list(map(int, input().split()))
    loai = data[0]
    
    if loai == 0:
        solve0(data[1])
    elif loai == 1:
        solve1(data[1], data[2])
    elif loai == 2:
        solve2(data[1], data[2])
    elif loai == 3:
        solve3()