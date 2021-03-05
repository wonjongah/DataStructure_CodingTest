from itertools import combinations

n, m = list(map(int, input().split()))
card_num = list(map(int, input().split()))

# 카드의 순열을 구한다.
card_cases = list(combinations(card_num, 3))
# 각 케이스마다의 합을 저장한다.
summary = []

# 각 카드의 순열의 합이 m보다 크면 다음 카드 순열을 불러오고,
# 작거나 같다면 합의 배열에 추가한다.
for case in card_cases:
    if sum(case) > m:
        continue
    else:
        summary.append(sum(case))

# 각 합의 제일 큰 값을 리턴한다.
print(max(summary))