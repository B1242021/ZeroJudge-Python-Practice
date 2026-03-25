while True:
    try:
        z = [0,0,0]
        n = int(input())
        for i in range(n):
            nub = int(input())
            if nub%3==0:
                z[0]+=1
            elif nub%3==1:
                z[1]+=1
            else:
                z[2]+=1
        print(" ".join(map(str,z)))
    except EOFError:
        break
        
        
