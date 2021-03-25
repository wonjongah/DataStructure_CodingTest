def solution(a, b):
    answer = ''
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    start_days = ["FRI"]
    for i in range(a):
        month_start_day = days.index(start_days[-1])
        if month[i] == 31:
            plus_day = 3
        elif month[i] == 30:
            plus_day = 2
        else:
            plus_day = 1
        month_index = month_start_day + plus_day
        if month_index >= 7:
            month_index = month_index - 7
        start_days.append(days[month_index])
                
    # 31이면 3번 째 요일, 30이면 2번째 후, 29면 1번째 후 요일에 끝남

    n = b % 7
    start_day = days.index(start_days[a - 1])
    
    index = start_day + (n - 1)
    if index >= 7:
        index = index - 7
    answer = days[index]
    return answer