n=int(input())
a=0
if n<=15:
    for v in range(5, 0, -1):
        if v <= n:
            n = n-v
            a = a+1

print(a)