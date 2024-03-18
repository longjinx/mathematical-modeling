num = list(map(int, input().split()))
n = num[0]
k = num[1]
juice = list(map(int, input().split()))
answer = 0

juice2 = list(dict.fromkeys(juice))

if len(juice2) < k:
    print(-1)
else:
    for m in range(1,len(juice2)):
        index = juice.index(juice2[m])
        answer += (index - m)

print(answer)
