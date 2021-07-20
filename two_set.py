n = int(input())
target = n*(n+1)
sum_list = []
num_list = []
if target%4!=0:
    print('NO')
else:
    target = target/4
    for i in range(n,0,-1):
        if i<=target:
            sum_list.append(i)
            target-=i
        else:
            num_list.append(i)
    if target==0:
        print('YES')
        print(len(sum_list))
        for i in sum_list:
            print(i, end=' ')
        print('')
        print(len(num_list))
        for i in num_list:
            print(i, end=' ')
    else:
        print('NO')

from new import fun
print(fun(10))