li = [1, 2, 3, 4, 5, 1, 2, 3]
new_li = []
for a in li:
    if a not in new_li:
        new_li.append(a)
print(new_li)