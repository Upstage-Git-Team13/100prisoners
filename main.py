
def prison_escape_simulation(boxes):
    for prisoner_number in range(1, 101):
        if not prisoner_attempt(prisoner_number, boxes):
            return False  # 하나라도 실패하면 전체 실패
    return True  # 모든 죄수가 성공
# 2. 개별 죄수의 시도
# 2번 팀원 코드
def prisoner_attempt(prisoner_number, boxes):
    max_attempts = 50  # 최대 50회 시도
    current_box = prisoner_number  # 첫 시도는 자신의 번호 상자
    attempts = 0  # 시도 횟수 초기화
    
    while attempts < max_attempts:
        attempts += 1
        current_number = boxes[current_box - 1]  # 상자 안의 번호 확인
        if current_number == prisoner_number:  # 자신 번호 발견 시 성공
            return True
        current_box = current_number  # 다음 상자
    
    return False  # 50회 이상 시도 후 실패

def get_success_percentage(nth: int) -> int:
    
    successfully_escaped = 0
    
    for _ in range(nth):
        suffled_boxes = suffle_box()
        
        if prison_escape_simulation(suffled_boxes): 
           successfully_escaped += 1
    
    rate = successfully_escaped / nth * 100
    return  "죄수들은 %f % 확률로 성공합니다." % (math.floor(rate))
        
