from itertools import combinations

n, m = list(map(int, input().split()))
card_num = list(map(int, input().split()))

card_cases = list(combinations(card_num, 3))
summary = []

for case in card_cases:
    if sum(case) > m:
        continue
    else:
        summary.append(sum(case))

print(max(summary))