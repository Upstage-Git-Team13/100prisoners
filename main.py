# 3. 전체 시뮬레이션
# 3번 팀원 코드
def prison_escape_simulation(boxes):
    for prisoner_number in range(1, 101):
        if not prisoner_attempt(prisoner_number, boxes):
            return False  # 하나라도 실패하면 전체 실패
    return True  # 모든 죄수가 성공
