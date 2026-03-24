"""1:1
2 1
3 10 5 16 8 4 2 1
4 2 1
5 16 8 4 2 1
6 3 16 8 4 2 1
7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
8 4 2 1
9 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
10 5 16 8 4 2 1"""

def apply(n):#正常情況
    sum=1
    while True:
        if n==1:
            break
        elif n/2==1:
            sum +=1
            break
        elif n%2==0:
            n//=2
        else:
            n = n*3+1
        sum +=1
    return sum
def max_cycle(a, b):
    max = 0
    for i in range(a,b+1):
        current = apply(i)
        if current>max:
            max = current
    return max
while True:
    try:
        i,j = map(int,input().split())
        if i>j:
            i,j = j,i
            print(j,i,max_cycle(i,j))
        elif i==j:
            print(i,j,apply(i))
        else:
            print(i, j, max_cycle(i,j))
    except EOFError:
        break
