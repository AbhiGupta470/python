'''
$    $
$$   $$
$$$  $$$
$$$$ $$$$
$    $
$$   $$
$$$  $$$
$$$$ $$$$'''
N = int(input())
N = N//2
for i in range(0,2):
    d=N
    for j in range(1,N+1):
        for k in range(1,j+1):
            print("$",end="")
        for l in range(1,d+1):
            print(" ",end="")
        d-=1 
        for m in range(1,j+1):
            print("$",end="")
        print()
