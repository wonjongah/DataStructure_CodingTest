data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]

def get_max_value(data_list, capacity):
    data_list = sorted(data_list, key=lambda x : x[1] / x[0], reverse = True)
    total_value = 0
    # 어떤 물건이 어떻게 들어있는지
    details = list()

    for data in data_list:
        # 제한된 무게보다 넣으려는 물건 무게가 작다면 그냥 넣는다
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0], data[1], 1])
        # 제한된 무게보다 넣으려는 물건 무게가 크다면 쪼개서 넣는다
        else:
            # 몇 퍼센트를 넣었나?
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            details.append([data[0], data[1], fraction])
            # capacity는 0이 되기 때문에 생략
            break
    return total_value, details

print(get_max_value(data_list, 30))