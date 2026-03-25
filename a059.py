while True:
    try:
        a = int(input())
        for j in range(a):
            m = int(input())
            n = int(input())
            if m>n:m,n = n,m
            total = 0
            for i in range(n):
                if m<=i*i<=n:
                    total +=i*i
            print(f"Case {j+1}:" ,total)
    except:
        break
