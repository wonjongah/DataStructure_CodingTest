# 1001 Hello 출력하기

print("Hello")

# 1002 Hello World 출력하기

print("Hello", "World")

# 1003 Hello
# World 출력하기

print("Hello\nWorld")

# 1004 'Hello' 출력하기

print("'Hello'")

# 1005 "Hello World" 출력하기

print('"Hello World"')

# 1006 "!@#$%^&*()" 출력하기

print('"!@#$%^&*()"')

# 1007 "C:\Download\hello.cpp" 출력하기

print(r'"C:\Download\hello.cpp"')
# \\이나 \n이 있을 경우를 대비해 r을 붙임

# 1008 유니코드로
# ┌┬┐
# ├┼┤
# └┴┘
# 출력하기

print("\u250C\u252C\u2510\n\u251C\u253C\u2524\n\u2514\u2534\u2518")

# 1010 정수 1개 입력받아 그대로 출력하기

print(int(input("")))

# 1011 입력된 문자를 그대로 출력하기

print(input(""))

# 1012 입력된 실수값을 그대로 출력하기

float = float(input(""))
print("%.6f" %float)

# 1013 정수 2개 입력받아 그대로 출력하기

a, b = input("").split()
print(int(b), int(a))

# 1014 문자 2개 입력받아 순서 바꿔 출력하기

a, b = input("").split()
print(b, a)

# 1015 실수 입력받아 둘째 자리까지 출력하기

float = float(input(""))
print("%.2f" %float)

# 1017 정수 1개 입력받아 3번 출력하기

num = int(input(""))
print(num, num, num)

# 1018 시간 입력받아 그대로 출력하기

hour, minute = input("").split(":")
print(int(hour), int(minute), sep=":")
# 바로 print(input(""))으로 해도 결과물은 같긴 하다.
# 만일 시간, 분을 나눠받고 싶으면 위의 방식으로 하면 된다.

# 1019 연월일 입력받아 그대로 출력하기

year, month, day = input("").split(".")
print("%04d.%02d.%02d" %(int(year), int(month), int(day)))
# zfill 메소드를 이용해도 문자열에 0을 채울 수 있다.
# print(format(year.zfill(4), month.zfill(2), day.zfill(2), sep = ".")

# 1020 주민번호 입력받아 형태 바꿔 출력하기

jumin = input("")
jumin = jumin.replace("-", "")
print("%013d" %int(jumin))
# 위는 숫자로 취급했을 때, 밑은 문자열로 취급했을 때
# num1, num2 = input("").split("-")
# print(num1 + num2)

# 1021 단어 1개 입력받아 그대로 출력하기

print(input(""))

# 1022 문장 1개 입력받아 그대로 출력하기

print(input(""))

# 1023 실수 1개 입력받아 부분별로 출력하기

jung, sil = input("").split(".")
print(int(jung))
print(int(sil))

# 1024 단어 1개 입력받아 나누어 출력하기

string = input("")
for i in string:
    print("'{}'".format(i))
# +로 문자열을 연결해도 무방

# 1025 정수 1개 입력받아 나누어 출력하기

num = int(input(""))
print("[{}]".format(num // 10000 * 10000))
num = num % 10000
print("[{}]".format(num // 1000 * 1000))
num = num % 1000
print("[{}]".format(num // 100 * 100))
num = num % 100
print("[{}]".format(num // 10 * 10))
num = num % 10
print("[{}]".format(num))
# 혹은 문자열 그대로 출력해도 무방하다면
# num = input();
# print("[%d]".format(int(n[0]) * 10000));
# 각 문자열 배열을 활용해서 각 자리 수를 구한다. 즉, num // 10000 -> n[0]
# for문을 사용할 수도 있다.

#  1026 시분초 입력받아 분만 출력하기

hour, minute, second = input("").split(":")
print(int(minute))

# 1027 년월일 입력받아 형식 바꿔 출력하기

year, month, day = input("").split(".")
print("{0:02d}-{1:02d}-{2:04d}".format(int(day), int(month), int(year)))
# 이 문제 또한 zfill 메서드 활용 가능하다.

# 1028 정수 1개 입력받아 그대로 출력하기2

print(int(input("")))

# 1029 실수 1개 입력받아 그대로 출력하기2

float = float(input(""))
print("%.11f" %float)

# 1030 정수 1개 입력받아 그대로 출력하기3

print(int(input("")))

# 1031 10진 정수 입력받아 16진수로 출력하기1

num = int(input(""))
print("%o" %num)
# num = int(input(""))
# print(format(num, "o"))
# format을 활용해서 출력도 가능

# 1032 10진 정수 입력받아 16진수로 출력하기1

num = int(input(""))
print("%x" %num)
# num = int(input(""))
# print(format(num, "x"))
# format을 활용해서 출력도 가능

# 1033 10진 정수 입력받아 16진수로 출력하기2

num = str(hex(int(input(""))))
num = num.replace("0x", "").upper() # 슬라이싱도 가능
print(num)
# num = int(input(""))
# print(format(num, 'X'))
# format을 활용해서 출력도 가능, 대문자로 출력하고 싶다면 대문자를 두 번째 인수로

# 1034 8진 정수 1개 입력받아 10진수로 출력하기

num = input("")
# num = "0o" + num
# 접두어 추가해도 안 해도 된다
num = int(num, 8)
print(num)

# 1035 16진수 정수 1개 입력받아 8진수로 출력하기

num = input("")
# num = "0x" + num
# 접두어 추가해도 안 해도 된다
num = int(num, 16) # 10진수로 변환
print(format(num, "o"))
# print("%o" %num)
# 포맷팅으로도 가능

# 1036 영문자 1개 입력받아 10진수로 출력하기

print(ord(input("")))

# 1037 정수 입력받아 아스키 문자로 출력하기

print(chr(int(input(""))))

# 1038 정수 2개 입력받아 합 출력하기1

num1, num2 = input("").split()
print(int(num1) + int(num2))

# 1039 정수 2개 입력받아 합 출력하기2

num1, num2 = input("").split()
print(int(num1) + int(num2))

# 1040 정수 1개 입력받아 부호 바꿔 출력하기

num = int(input(""))
print(-1 * num)

# 1041 문자 1개 입력받아 다음 문자 출력하기

nextalpha = ord(input("")) + 1
print(chr(nextalpha))

# 1042 정수 2개 입력받아 나눈 몫 출력하기

num1, num2 = input("").split()
print(int(num1) // int(num2))

# 1043 정수 2개 입력받아 나눈 나머지 출력하기

num1, num2 = input("").split()
print(int(num1) % int(num2))

# 1044 정수 1개 입력받아 1개 더해 출력하기

print(int(input(""))+1)


# 1045 정수 2개 입력받아 자동 계산하기

num1, num2 = input("").split()
num1 = int(num1)
num2 = int(num2)
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 // num2)
print(num1 % num2)
print("%.2f" % (num1 / num2))

# 1046 정수 3개 입력받아 합과 평균 출력하기

num1, num2, num3 = input("").split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
plus = num1 + num2 + num3
print(plus)
print("%.1f" % (plus / 3))

# 1047 정수 1개 입력받아 2배 곱해 출력하기

num = int(input())
print(num << 1)

# 1048 한 번에 2의 거듭제곱 배로 출력하기(a 를 2b배 만큼 곱한 값을 출력한다.)

a, b = map(int, input().split())
print(a << b)
# a, b = map(int, input().split())
# print(a * (2 ** b))
# ** 연산으로도 가능

# 1049 두 정수 입력받아 비교하기1 (a가 b보다 큰 경우 1을, 그렇지 않은 경우 0을 출력한다.)

a, b = map(int, input().split())
print(int(a > b))
# 물론 if를 사용해도 무관

# 1050 두 정수 입력받아 비교하기2 (a와 b의 값이 같은 경우 1을, 그렇지 않은 경우 0을 출력한다.)

a, b = map(int, input().split())
print(int(a == b))

# 1051 두 정수 입력받아 비교하기3 (b가 a보다 크거나 같은 경우 1을, 그렇지 않은 경우 0을 출력한다.)

a, b = map(int, input().split())
print(int(b >= a))

# 1052 두 정수 입력받아 비교하기4 (a와 b가 다른 경우 1을, 그렇지 않은 경우 0을 출력한다.)

a, b = map(int, input().split())
print(int(a != b))

# 1053 참 거짓 바꾸기

num = int(input())
print(int(not num))
# 물론 if문도 가능

# 1054 둘 다 참일 경우만 참 출력하기 (둘 다 참(1)일 경우에만 1을 출력하고, 그 외의 경우에는 0을 출력한다.)

a, b = map(int, input().split())
print(int(a and b))
# 물론 if문도 가능

# 1055 하나라도 참이면 참 출력하기

a, b = map(int, input().split())
print(int(a or b))
# 물론 if문도 가능

# 1056 참 거짓이 서로 다를 때에만 참 출력하기(XOR)

a, b = map(int, input().split())
print(int((a and not b) or (not a and b)))
# 둘 중 하나를 일부러 역을 시켜서 다를 경우 찾기
# 둘이 1, 0 혹은 0, 1이 입력됐을 때만 참

# 1057 참 거짓이 서로 같을 때에만 참 출력하기

a, b = map(int, input().split())
print(int((not a and not b) or (a and b)))
# 둘 중 하나를 일부러 역을 시켜서 같을 경우 찾기
# 둘이 1, 1 혹은 0, 0이 입력됐을 때만 참

# 1058 둘 다 거짓일 경우만 참 출력하기

a, b = map(int, input().split())
print(int(not a and not b))
# print(int(not (a or b)))도 가능
# 둘 다 역으로 바꾸어 0, 0일 경우 찾기

# 1059 비트단위로 not하여 출력하기(~ 사용)

num = ~int(input())
print(num)

# 1060 비트단위로 and하여 출력하기(& 사용)

a, b = map(int, input().split())
print(a & b)

# 1061 비트단위로 or하여 출력하기(| 사용)

a, b = map(int, input().split())
print(a | b)

# 1062 비트단위로 xor하여 출력하기(^ 사용)

a, b = map(int, input().split())
print(a ^ b)

# 1063 두 정수 입력받아 큰 수 출력하기(삼항연산)

a, b = map(int, input().split())
print(a  if a > b else b) 
# print(max(a, b))도 가능

# 1064 정수 3개 입력받아 가장 작은 수 출력하기(삼항연산)

a, b, c = map(int, input().split())
print(min(a, b, c))
# 삼항연산보다 min 함수를 쓰는 게 더 간략하다.

# 1065 정수 3개 입력받아 짝수만 출력하기

a, b, c = map(int, input().split())
if(a % 2 == 0):
    print(a)
if(b % 2 == 0):
    print(b)
if(c % 2 == 0):
    print(c)

# a = map(int, input().split())
# for i in a:
#     if(i % 2 == 0):
#         print(i)

# 1066 정수 3개 입력받아 짝/홀 출력하기

a, b, c = map(int, input().split())

if x % 2 == 0:
    print("even")
else:
    print("odd")
if y % 2 == 0:
    print("even")
else:
    print("odd")
if z % 2 == 0:
    print("even")
else:
    print("odd")

# nums = map(int, input().split())
# for i in nums:
#     if i % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# 1067 [선택실행구조] 정수 1개 입력받아 분석하기

num = int(input())
if num > 0:
    print("plus")
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
else:
    print("minus")
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

# num = int(input())
# if num > 0:
#     print("plus")
# elif num < 0:
#     print("minus")
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

# 1068 정수 1개 입력받아 평가 출력하기

score = int(input())

if score <= 100 and score >= 90:
    print("A")
elif score >= 70:
    print("B")
elif score >= 40:
    print("C")
else:
    print("D")

# 1069 평가 입력받아 다르게 출력하기

alpha = input()

if alpha == "A":
    print("best!!!")
elif alpha == "B":
    print("good!!")
elif alpha == "C":
    print("run!")
elif alpha == "D":
    print("slowly~")
else:
    print("what?")

# 1070 월 입력받아 계절 출력하기

month = int(input())

if month in [12, 1, 2]:
    print("winter")
elif month in [3, 4, 5]:
    print("spring")
elif month in [6, 7, 8]:
    print("summer")
elif month in [9, 10, 11]:
    print("fall")

# if-elif과 or을 사용해 해결도 가능

# 1071 0 입력될 때까지 무한 출력하기 1

nums = map(int, input().split())

for i in nums:
    if not i == 0:
        print(i)
    else:
        break

# 1072 정수 입력받아 계속 출력하기

count = int(input())
nums = input().split()

for i in nums:
    print(i)

# 1073 0 입력될 때까지 무한 출력하기 2

nums = list(map(int, input().split()))
count = 0
while(nums[count] != 0):
    print(nums[count])
    count += 1

# int() 함수를 쓰지 않고 문자열 비교로 == "0"으로 해도 무방
# for문 써도 무방
# nums = map(int, input().split())
# for i in nums:
#     if not i == 0:
#         print(i)
#     else:
#         break

# 1074 정수 1개 입력받아 카운트다운 출력하기1

count = int(input())
while(count != 0):
    print(count)
    count -= 1

# for문도 가능

# 1075 정수 1개 입력받아 카운트다운 출력하기2

count = int(input())
while(count > 0):
    count -= 1
    print(count)

# 1076 문자 1개 입력받아 알파벳 출력하기

alpha = input()
for i in range(ord("a"), ord(alpha) + 1):
    print(chr(i), end=" ")

# 1077 정수 1개 입력받아 그 수까지 출력하기

count = int(input())
for i in range(count + 1):
    print(i)

# 1078 짝수 합 구하기

num = int(input())
sum = 0
for i in range(0, num + 1, 2):
    sum += i
print(sum)

# 1079 원하는 문자가 입력될 때까지 반복 출력하기

a = input().split()
for i in a:
    print(i)
    if i == "q":
        break

# 1080 언제까지 더해야 할까?

num = int(input())
sum = 0
for i in range(0, num):
    sum += i
    if sum >= num:
        print(i)
        break

# 1081 주사위 2개를 던지면?

a, b = input().split()
for i in range(1, int(a) + 1):
    for j in range(1, int(b) + 1):
        print(i, j)

# 1082


# 1083 3 6 9 게임의 왕이 되자!

num = int(input())

for i in range(1, num + 1):
    if i % 3 == 0:
        print("X", end=" ")
    else:
        print(i, end=" ")

# 1088 3의 배수는 통과?

num = int(input())

for i in range(1, num + 1):
    if i % 3 == 0:
        continue
    else:
        print(i, end = " ")

# 1084 빛 섞어 색 만들기

red, green, blue = map(int, input().split())

count = 0

for r in range(red):
    for g in range(green):
        for b in range(blue):
            print(r, g, b)
            count += 1

print(count)
# print(red * green * blue)

# 1085 소리 파일 저장용량 계산하기

h, b, c, s = map(int, input().split())
result = h * b * c * s / 8 / 1024 / 1024
print(round(result, 1), "MB")

# 1086 그림 파일 저장용량 계산하기

w, h, b = map(int, input().split())
result = w * h * b / 8 / 1024 /1024
print(f"{result:.2f} MB")
# codeup 페이지는 f 포맷이 지원되지 않는 모양, 밑도 가능
# w, h, b = map(int, input().split())
# result = w * h * b / 8 / 1024 /1024
# print("{0:.2f} MB".format(result))

# 1087 여기까지! 이제 그만~

num = int(input())

sum = 0
count = 1
while True:
    sum += count
    count += 1
    if sum >= num:
        break
print(sum)

# 1089 수 나열하기 1

a, d, n = map(int, input().split())
for i in range(n - 1):
    a += d
print(a)

# 1090 수 나열하기 2

a, d, n = map(int, input().split())
for i in range(n - 1):
    a *= d
print(a)