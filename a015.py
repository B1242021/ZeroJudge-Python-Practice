while True:
    try:
        m, n = map(int, input().split())
        A = []
        for _ in range(m):
            row = list(map(int, input().split()))
            A.append(row)
        for c in range(n):
            for r in range(m):
                print(A[r][c], end=" ")
            print()
    except EOFError:
        break
