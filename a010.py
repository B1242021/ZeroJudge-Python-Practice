n = int(input())
i = 2
sol = {}
while i <=n:
    while n%i==0:
        sol[i] = sol.get(i,0)+1
        n=n/i
    i+=1
if n>1:
    sol[i] = sol.get(i,0)+1
ans = []
for prime in sol:
    if sol[prime] ==1:
        ans.append(str(prime))
    else:
        ans.append(f"{prime}^{sol[prime]}")
a = " * ".join(ans)
print(a)
