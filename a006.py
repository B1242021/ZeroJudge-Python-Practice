a,b,c = map(int,input().split())
z = b**2-4*a*c
if z<0:
    print("No real root")
elif z == 0:
    root = int(-b/(2*a))
    print(f"Two same roots x={root}")
else:
    root1 = int((-b+z**0.5)/2*a)
    root2 = int((-b-z**0.5)/2*a)
    if root1<root2:
        root1,root2 = root2,root1
    print(f"Two different roots x1={root1} , x2={root2}")
