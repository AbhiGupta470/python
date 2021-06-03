'''    1 
      1 1 
     1 2 1 
    1 3 3 1 
   1 4 6 4 1 
  1 5 10 10 5 1 
 1 6 15 20 15 6 1 
1 7 21 35 35 21 7 1'''
#code for this type of pattern
def factorial(num):
    f = 1
    if num>=1:
        for v in range(1,num+1):
            f=f*v
    return f

n = int(input())
n = n-1
for j in range(n+1):
    print(" " * (n-j), end="")

    for k in range(j+1):
        a = factorial(j)
        b = factorial(k)
        c= factorial(j-k)
        c=a/(b*c)
        c=int(c)
        print(str(c)+" ",end="")
    print()
