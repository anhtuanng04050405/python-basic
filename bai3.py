arr = list(map(int, input("Nhập mảng: ").split()))
ans = 0
for i in range(len(arr)):
    if(arr[i]%2==0):
        ans=ans+1
print(ans)