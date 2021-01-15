num = input("")
num = "0x" + num # 접두어 추가
num = int(num, 16) # 10진수로 변환
print(format(num, "o"))

# f -> 17
