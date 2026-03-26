while True:
    try:
        n,m = map(int,input().split())
        if n == m:
            days = m
        else:
            days = m+1
        print(days)
    except EOFError:
        break
