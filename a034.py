while True:
    try:
        n = int (input())
        lst =[]
        while n>=1:
            lst.append(str(n%2))
            n = n//2
        lst.reverse()
        print("".join(lst))
    except EOFError:
        break
