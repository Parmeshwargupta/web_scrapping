import time
start = time.time()
found = -1
l = [1, 2, 3, 1, 4]
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] == l[j]:
            found = l[i]
print(found)
end = time.time()
print(1000*(end-start))
