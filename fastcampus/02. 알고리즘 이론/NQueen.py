def is_available(candidate, current_col):
    # candidate의 개수로 현재 행을 알 수 있다.
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True

# current_row - 현재 행, current_candidate - 지금까지 위치 정보
def DFS(N, current_row, current_candidate, final_result):
    # 종료 조건, 배치가 다 끝났을 때
    if current_row == N:
        final_result.append(current_candidate[:])
        return

    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row + 1, current_candidate, final_result)
            # 마지막도 아니고, 조건에 맞지 않는다면 그냥 return
            current_candidate.pop()
            # 가능한 것에서 제외

def solve_n_queen(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result

print(solve_n_queen(4))