def solution(a, b):
    answer = ''
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["SUN","MON","TUE","WED","THU","FRI","SAT"]

    if a > 1:
        for i in range(a - 1):
            b += month[i]

    n = b % 7
    start_day = 5
    index = start_day + (n - 1)
    answer = days[index % 7]

    return answer