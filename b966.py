while True:
    try:
        line =[]
        a = int(input())
        for _ in range(a):
            m,n = map(int,input().split())
            if m>n:n,m=m,n
            line.append([m,n])
        line.sort()
        total =0
        current_start = line[0][0]
        current_end = line[0][1]
        for i in range(1,len(line)):
            next_start = line[i][0]
            next_end = line[i][1]
            if next_start<=current_end:
                current_end =max(current_end,next_end)
            else:
                total += current_end - current_start
                current_start = line[i][0]
                current_end = line[i][1]
        total+=current_end - current_start
        print(total)
    except EOFError:
        break
