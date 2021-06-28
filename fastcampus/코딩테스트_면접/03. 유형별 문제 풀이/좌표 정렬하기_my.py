num = int(input())
li = list()
for _ in range(num):
    x, y = map(int, input().split())
    li.append((x, y))

li.sort()
for i in li:
    print(i[0], i[1])