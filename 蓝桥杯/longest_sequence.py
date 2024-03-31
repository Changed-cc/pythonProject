S = input().upper().rstrip(' ')
T = input().upper().rstrip(' ')
count = 0
max_count = 0

for i in range(len(T)):
    count = 0
    for j in range(len(S)):
        if j+i < len(T) and T[i+j] == S[j]:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0

print(max_count)



