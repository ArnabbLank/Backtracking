st = input()
st_list = []
count = 0
n = len(st)
i = 0
temp_count = 0
while i < n-1:
    if st[i] ==st[i+1]:
        count+=1
    else: 
        count = 0
    if temp_count<count:
        temp_count = count
    i+= 1
print(temp_count+1)

