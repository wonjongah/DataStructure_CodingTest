def bigchange(n):
    count = 0
    coin_types = [500, 100, 50, 10]
    for coin in coin_types:
        count += n // coin # 해당 화폐로 거슬러줄 수 있는 동전의 개수 세기
        n %= coin
    return count

n = 1260
print(bigchange(n))