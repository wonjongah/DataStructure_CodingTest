a = list(map(int, input().split()))

ascending = True
descending = True

for i in range(1, 8):
    # 앞 값이 뒤의 값보다 작으면 내림차순은 아니다.
    if a[i] > a[i - 1]:
        descending = False
    # 앞 값이 뒤의 값보다 크면 오른차순은 아니다.
    elif a[i] < a[i - 1]:
        ascending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")