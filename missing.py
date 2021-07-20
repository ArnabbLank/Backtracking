n = int(input())
l = list(map(int, input().split()))
l1 = {}
for i in range(n):
    l1[i+1] = 0
for i in l:
    l1[i] = 1
for j in l1.keys():
    if l1[j] == 0:
        print(j)