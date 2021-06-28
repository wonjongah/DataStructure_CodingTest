num = int(input())
nums = list()

for _ in range(num):
    nums.append(int(input()))

nums.sort()
for i in nums:
    print(i)