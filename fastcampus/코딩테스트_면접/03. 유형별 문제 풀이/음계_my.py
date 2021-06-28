li = list(map(int, input().split()))
ascending = [1,2,3,4,5,6,7,8]

if li == ascending:
    print("ascending")
elif li == list(reversed(ascending)):
    print("descending")
else:
    print("mixed")