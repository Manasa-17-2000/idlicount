N = int(input("enter the number : "))
for i in range(N):
    a,b,k = (map(int, input().split()))
    if a >= b:
        print(k//b)
    else:
        print(k//a)
