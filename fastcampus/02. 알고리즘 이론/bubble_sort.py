import random

def bubblesort(data):
    for index1 in range(len(data) - 1): # 턴
        swap = False
        for index2 in range(len(data) - index1 - 1): # 조건체크
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True
        if swap == False: # 정렬 다 되었으면, 바뀔 게 더 없다면
            break
    return data

data_list = random.sample(range(100), 50)
print("정렬 전")
print(data_list)
print("정렬 후")
print(bubblesort(data_list))