num = list(map(int, input().split()))
n = num[0]
k = num[1]
juice = list(map(int, input().split()))
answer = 0

juice2 = list(dict.fromkeys(juice))
# print(f"去重juice2是{juice2}")
lst = []
dic = {}

if len(juice2) < k:
    print(-1)
else:
    for i in range(len(juice)):
        if juice[i] in dic:
            # print("已在字典里")
            pass
        else:
            # print("不在字典里")
            answer += (i-len(dic))
            # print(i)
            # print(f"这个数增加的answer是{i-len(dic)}")
            # print(f"现answer是{answer}")
            dic[juice[i]] = i
            # print(dic)

    print(answer)
