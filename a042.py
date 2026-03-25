while True:
    try:
        n = int(input())
        if n==1:
            total =2
        else:
            total =2
            for i in range(1,n):
                total = total + 2*i
        print(total)
    except EOFError:
        break
