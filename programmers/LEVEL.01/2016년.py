def solution(a, b):
    answer = ''
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    start_days = ["FRI", "MON", "TUE", "FRI", "SUN", "WED", "FRI", "MON", "THU", "SAT", "TUE", "THU"]
    
    n = b % 7
    start_day = days.index(start_days[a - 1])
    
    index = start_day + (n - 1)
    if index >= 7:
        index = index - 7
    answer = days[index]
    return answer