origin = list(input())
aim = list(input())

num = 0


def change(lst, n):
    lst[n], lst[n + 1] = lst[n + 1], lst[n]
    return lst


for i in range(len(origin)):
    if origin[i] != aim[i]:
        change(origin, i)
        num += 1

print(num)
