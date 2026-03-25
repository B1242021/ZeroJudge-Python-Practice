a, b =map(int, input().split())
if a>b:a,b=b,a
sum=[]
ans =0
for i in range(a, b+1):
    total = 0
    ln = str(i)
    for x in ln:
        ans = int(x)**int(len(ln))
        total+=ans
    if total ==i:
        sum.append(i)
if len(sum)!=0:
    print(*sum)
else:
    print('none')
