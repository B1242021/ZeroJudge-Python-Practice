def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
num1, num2 = map(int, input().split())
print(gcd(num1, num2))
