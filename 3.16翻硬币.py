origin = list(input().strip())
aim = list(input().strip())

num = 0

def change(lst, n):
    if lst[n] == "o" and lst[n + 1] == "*":
        lst[n] = "*"
        lst[n + 1] = "o"
    elif lst[n] == "o" and lst[n + 1] == "o":
        lst[n] = "*"
        lst[n + 1] = "*"
    elif lst[n] == "*" and lst[n + 1] == "o":
        lst[n] = "o"
        lst[n + 1] = "*"
    elif lst[n] == "*" and lst[n + 1] == "*":
        lst[n] = "o"
        lst[n + 1] = "o"


for i in range(len(origin)):
    if origin[i] != aim[i]:
        change(origin, i)
        num += 1

print(num)
