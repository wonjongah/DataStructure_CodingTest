num = int(input())
users = list()
for _ in range(num):
    age, name = input().split()
    # age int로 변형하는 것 잊지 않기
    users.append([int(age), name])
users = sorted(users, key=lambda x: x[0])
# user.sort(key=lambda x:x[0])
# 첫 번째 요소 같으면, 두 번째 요소 기준으로 정렬
# users.sort(key = lambda x: [x[0], x[1]])
for i in users:
    print(i[0], i[1])