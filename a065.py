while True:
    try:
        z =""
        a = input().upper()
        for i in range(1,len(a)):
            x = abs(ord(a[i])-ord(a[i-1]))
            z += str(x)
        print(*z,sep="")
    except EOFError:
        break
