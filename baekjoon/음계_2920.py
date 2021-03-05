li = list(map(int, input().split()))
ascending = [1,2,3,4,5,6,7,8]

if li == ascending:
    print("ascending")
# 순차배열의 반대로 정렬된 리스트와 같다면
elif li == list(reversed(ascending)):
    print("descending")
else:
    print("mixed")