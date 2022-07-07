n = input()
a = list(map(int, input().split()))
sum = sum(a)
a.sort(reverse=True)
su = 0
result = 0
for i in range(len(a)):
    if su <= sum:
        su+=a[i]
        sum-=a[i]
        result+=1
print(result)
