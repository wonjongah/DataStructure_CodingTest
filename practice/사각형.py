def solution(v):
    x = []
    y = []
    
    for i in v:
        x.append(i[0])
        y.append(i[1])
        if x.count(i[0]) == 2:
            x = list(set(x))
            x.remove(i[0])
        if y.count(i[1]) == 2:
            y = list(set(y))
            y.remove(i[1])
    x.extend(y)
    return x

print(solution([[1, 4], [3, 4], [3, 10]]))