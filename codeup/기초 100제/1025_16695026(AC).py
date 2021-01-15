[70000]
[5000]
[200]
[50]
[4]
num = int(input(""))
print("[{}0000]".format(num // 10000))
num = num % 10000
print("[{}000]".format(num // 1000))
num = num % 1000
print("[{}00]".format(num // 100))
num = num % 100
print("[{}0]".format(num // 10))
num = num % 10
print("[{}]".format(num))
