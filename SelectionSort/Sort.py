import time

some_list = [4,3,6,2]
i = 0
x = 0
smallest_value = i
for i in range(len(some_list)):
    for j in range(i+1,len(some_list)):
        if some_list[j] < some_list[smallest_value]:
            smallest_value = j
        some_list[smallest_value], some_list[i] = some_list[i], some_list[smallest_value]
        x+=1
time.sleep(1)
print(some_list)
print x