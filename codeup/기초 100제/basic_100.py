# 1001 Hello ����ϱ�

print("Hello")

# 1002 Hello World ����ϱ�

print("Hello", "World")

# 1003 Hello
# World ����ϱ�

print("Hello\nWorld")

# 1004 'Hello' ����ϱ�

print("'Hello'")

# 1005 "Hello World" ����ϱ�

print('"Hello World"')

# 1006 "!@#$%^&*()" ����ϱ�

print('"!@#$%^&*()"')

# 1007 "C:\Download\hello.cpp" ����ϱ�

print(r'"C:\Download\hello.cpp"')
# \\�̳� \n�� ���� ��츦 ����� r�� ����

# 1008 �����ڵ��
# ������
# ������
# ������
# ����ϱ�

print("\u250C\u252C\u2510\n\u251C\u253C\u2524\n\u2514\u2534\u2518")

# 1010 ���� 1�� �Է¹޾� �״�� ����ϱ�

print(int(input("")))

# 1011 �Էµ� ���ڸ� �״�� ����ϱ�

print(input(""))

# 1012 �Էµ� �Ǽ����� �״�� ����ϱ�

float = float(input(""))
print("%.6f" %float)

# 1013 ���� 2�� �Է¹޾� �״�� ����ϱ�

a, b = input("").split()
print(int(b), int(a))

# 1014 ���� 2�� �Է¹޾� ���� �ٲ� ����ϱ�

a, b = input("").split()
print(b, a)

# 1015 �Ǽ� �Է¹޾� ��° �ڸ����� ����ϱ�

float = float(input(""))
print("%.2f" %float)

# 1017 ���� 1�� �Է¹޾� 3�� ����ϱ�

num = int(input(""))
print(num, num, num)

# 1018 �ð� �Է¹޾� �״�� ����ϱ�

hour, minute = input("").split(":")
print(int(hour), int(minute), sep=":")
# �ٷ� print(input(""))���� �ص� ������� ���� �ϴ�.
# ���� �ð�, ���� �����ް� ������ ���� ������� �ϸ� �ȴ�.

# 1019 ������ �Է¹޾� �״�� ����ϱ�

year, month, day = input("").split(".")
print("%04d.%02d.%02d" %(int(year), int(month), int(day)))
# zfill �޼ҵ带 �̿��ص� ���ڿ��� 0�� ä�� �� �ִ�.
# print(format(year.zfill(4), month.zfill(2), day.zfill(2), sep = ".")

# 1020 �ֹι�ȣ �Է¹޾� ���� �ٲ� ����ϱ�

jumin = input("")
jumin = jumin.replace("-", "")
print("%013d" %int(jumin))
# ���� ���ڷ� ������� ��, ���� ���ڿ��� ������� ��
# num1, num2 = input("").split("-")
# print(num1 + num2)

# 1021 �ܾ� 1�� �Է¹޾� �״�� ����ϱ�

print(input(""))

# 1022 ���� 1�� �Է¹޾� �״�� ����ϱ�

print(input(""))

# 1023 �Ǽ� 1�� �Է¹޾� �κк��� ����ϱ�

jung, sil = input("").split(".")
print(int(jung))
print(int(sil))

# 1024 �ܾ� 1�� �Է¹޾� ������ ����ϱ�

string = input("")
for i in string:
    print("'{}'".format(i))
# +�� ���ڿ��� �����ص� ����

# 1025 ���� 1�� �Է¹޾� ������ ����ϱ�

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
# Ȥ�� ���ڿ� �״�� ����ص� �����ϴٸ�
# num = input();
# print("[%d]".format(int(n[0]) * 10000));
# �� ���ڿ� �迭�� Ȱ���ؼ� �� �ڸ� ���� ���Ѵ�. ��, num // 10000 -> n[0]
# for���� ����� ���� �ִ�.

#  1026 �ú��� �Է¹޾� �и� ����ϱ�

hour, minute, second = input("").split(":")
print(int(minute))

# 1027 ����� �Է¹޾� ���� �ٲ� ����ϱ�

year, month, day = input("").split(".")
print("{0:02d}-{1:02d}-{2:04d}".format(int(day), int(month), int(year)))
# �� ���� ���� zfill �޼��� Ȱ�� �����ϴ�.

# 1028 ���� 1�� �Է¹޾� �״�� ����ϱ�2

print(int(input("")))

# 1029 �Ǽ� 1�� �Է¹޾� �״�� ����ϱ�2

float = float(input(""))
print("%.11f" %float)

# 1030 ���� 1�� �Է¹޾� �״�� ����ϱ�3

print(int(input("")))

# 1031 10�� ���� �Է¹޾� 16������ ����ϱ�1

num = int(input(""))
print("%o" %num)
# num = int(input(""))
# print(format(num, "o"))
# format�� Ȱ���ؼ� ��µ� ����

# 1032 10�� ���� �Է¹޾� 16������ ����ϱ�1

num = int(input(""))
print("%x" %num)
# num = int(input(""))
# print(format(num, "x"))
# format�� Ȱ���ؼ� ��µ� ����

# 1033 10�� ���� �Է¹޾� 16������ ����ϱ�2

num = str(hex(int(input(""))))
num = num.replace("0x", "").upper() # �����̵̽� ����
print(num)
# num = int(input(""))
# print(format(num, 'X'))
# format�� Ȱ���ؼ� ��µ� ����, �빮�ڷ� ����ϰ� �ʹٸ� �빮�ڸ� �� ��° �μ���

# 1034 8�� ���� 1�� �Է¹޾� 10������ ����ϱ�

num = input("")
# num = "0o" + num
# ���ξ� �߰��ص� �� �ص� �ȴ�
num = int(num, 8)
print(num)

# 1035 16���� ���� 1�� �Է¹޾� 8������ ����ϱ�

num = input("")
# num = "0x" + num
# ���ξ� �߰��ص� �� �ص� �ȴ�
num = int(num, 16) # 10������ ��ȯ
print(format(num, "o"))
# print("%o" %num)
# ���������ε� ����

# 1036 ������ 1�� �Է¹޾� 10������ ����ϱ�

print(ord(input("")))

# 1037 ���� �Է¹޾� �ƽ�Ű ���ڷ� ����ϱ�

print(chr(int(input(""))))

# 1038 ���� 2�� �Է¹޾� �� ����ϱ�1

num1, num2 = input("").split()
print(int(num1) + int(num2))

# 1039 ���� 2�� �Է¹޾� �� ����ϱ�2

num1, num2 = input("").split()
print(int(num1) + int(num2))

# 1040 ���� 1�� �Է¹޾� ��ȣ �ٲ� ����ϱ�

num = int(input(""))
print(-1 * num)

# 1041 ���� 1�� �Է¹޾� ���� ���� ����ϱ�

nextalpha = ord(input("")) + 1
print(chr(nextalpha))

# 1042 ���� 2�� �Է¹޾� ���� �� ����ϱ�

num1, num2 = input("").split()
print(int(num1) // int(num2))

# 1043 ���� 2�� �Է¹޾� ���� ������ ����ϱ�

num1, num2 = input("").split()
print(int(num1) % int(num2))

# 1044 ���� 1�� �Է¹޾� 1�� ���� ����ϱ�

print(int(input(""))+1)


# 1045 ���� 2�� �Է¹޾� �ڵ� ����ϱ�

num1, num2 = input("").split()
num1 = int(num1)
num2 = int(num2)
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 // num2)
print(num1 % num2)
print("%.2f" % (num1 / num2))

# 1046 ���� 3�� �Է¹޾� �հ� ��� ����ϱ�

num1, num2, num3 = input("").split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
plus = num1 + num2 + num3
print(plus)
print("%.1f" % (plus / 3))

# 1047 ���� 1�� �Է¹޾� 2�� ���� ����ϱ�

num = int(input())
print(num << 1)

# 1048 �� ���� 2�� �ŵ����� ��� ����ϱ�(a �� 2b�� ��ŭ ���� ���� ����Ѵ�.)

a, b = map(int, input().split())
print(a << b)
# a, b = map(int, input().split())
# print(a * (2 ** b))
# ** �������ε� ����

# 1049 �� ���� �Է¹޾� ���ϱ�1 (a�� b���� ū ��� 1��, �׷��� ���� ��� 0�� ����Ѵ�.)

a, b = map(int, input().split())
print(int(a > b))
# ���� if�� ����ص� ����

# 1050 �� ���� �Է¹޾� ���ϱ�2 (a�� b�� ���� ���� ��� 1��, �׷��� ���� ��� 0�� ����Ѵ�.)

a, b = map(int, input().split())
print(int(a == b))

# 1051 �� ���� �Է¹޾� ���ϱ�3 (b�� a���� ũ�ų� ���� ��� 1��, �׷��� ���� ��� 0�� ����Ѵ�.)

a, b = map(int, input().split())
print(int(b >= a))

# 1052 �� ���� �Է¹޾� ���ϱ�4 (a�� b�� �ٸ� ��� 1��, �׷��� ���� ��� 0�� ����Ѵ�.)

a, b = map(int, input().split())
print(int(a != b))

# 1053 �� ���� �ٲٱ�

num = int(input())
print(int(not num))
# ���� if���� ����

# 1054 �� �� ���� ��츸 �� ����ϱ� (�� �� ��(1)�� ��쿡�� 1�� ����ϰ�, �� ���� ��쿡�� 0�� ����Ѵ�.)

a, b = map(int, input().split())
print(int(a and b))
# ���� if���� ����

# 1055 �ϳ��� ���̸� �� ����ϱ�

a, b = map(int, input().split())
print(int(a or b))
# ���� if���� ����

# 1056 �� ������ ���� �ٸ� ������ �� ����ϱ�(XOR)

a, b = map(int, input().split())
print(int((a and not b) or (not a and b)))
# �� �� �ϳ��� �Ϻη� ���� ���Ѽ� �ٸ� ��� ã��
# ���� 1, 0 Ȥ�� 0, 1�� �Էµ��� ���� ��

# 1057 �� ������ ���� ���� ������ �� ����ϱ�

a, b = map(int, input().split())
print(int((not a and not b) or (a and b)))
# �� �� �ϳ��� �Ϻη� ���� ���Ѽ� ���� ��� ã��
# ���� 1, 1 Ȥ�� 0, 0�� �Էµ��� ���� ��

# 1058 �� �� ������ ��츸 �� ����ϱ�

a, b = map(int, input().split())
print(int(not a and not b))
# print(int(not (a or b)))�� ����
# �� �� ������ �ٲپ� 0, 0�� ��� ã��

# 1059 ��Ʈ������ not�Ͽ� ����ϱ�(~ ���)

num = ~int(input())
print(num)

# 1060 ��Ʈ������ and�Ͽ� ����ϱ�(& ���)

a, b = map(int, input().split())
print(a & b)

# 1061 ��Ʈ������ or�Ͽ� ����ϱ�(| ���)

a, b = map(int, input().split())
print(a | b)

# 1062 ��Ʈ������ xor�Ͽ� ����ϱ�(^ ���)

a, b = map(int, input().split())
print(a ^ b)

# 1063 �� ���� �Է¹޾� ū �� ����ϱ�(���׿���)

a, b = map(int, input().split())
print(a  if a > b else b) 
# print(max(a, b))�� ����

# 1064 ���� 3�� �Է¹޾� ���� ���� �� ����ϱ�(���׿���)

a, b, c = map(int, input().split())
print(min(a, b, c))
# ���׿��꺸�� min �Լ��� ���� �� �� �����ϴ�.

# 1065 ���� 3�� �Է¹޾� ¦���� ����ϱ�

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
