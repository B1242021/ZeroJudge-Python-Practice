while True:
    try:
        n = int(input())
        if n==1:
            total =2
        else:
            total = int((n*n*n+5*n+6)/6)
        print(total)
    except EOFError:
        break
