while True:
    try:
        n = int(input())
        if 1<= n <=10:
            nub = n*6
        elif 11<=n<=20:
            nub = 60+(n-10)*2
        elif 21<=n<=40:
            nub = 80+(n-20)
        elif n ==0:
            nub = 0
        else:
            nub =100
        print(nub)
    except EOFError:
        break
