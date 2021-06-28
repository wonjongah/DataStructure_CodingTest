coin_list = [500, 100, 50, 1]

def min_coin_count(value, coin_list):
    total_coin_count = 0
    # 어떤 동전이 얼마나 쓰였는지
    details = list()
    coin_list.sort(reverse=True) # 큰 순서대로 정렬
    # 동전의 개수를 적게 하려면, 큰 동전으로 값을 줄이면 좋기 때문
    for coin in coin_list:
        coin_num = value // coin
        total_coin_count += coin_num
        value -= coin_num * coin
        details.append([coin, coin_num])
    return total_coin_count, details

print(min_coin_count(4720, coin_list))