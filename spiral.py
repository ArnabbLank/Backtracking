t = int(input())
for i in range(t):
    r, c = list(map(int, input().split()))
    if r > c:
        if r%2 == 0:
            num = (r*r)-c+1
        else:
            num = (r-1)*(r-1)+c
    else:
        if c%2==0:
            num = (c-1)*(c-1)+r
        else:
            num = (c*c)-r+1
    print(num)