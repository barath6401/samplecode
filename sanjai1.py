val = list(input())
k = int(input())
ans = []
for i in range(0, len(val)):
    if int(val[i])%2 == 0:
        p = (i+k)%len(val)
        ans.append(val[p])
    else:
        ans.append(val[i])
for i in ans:
    print(i,end='')
