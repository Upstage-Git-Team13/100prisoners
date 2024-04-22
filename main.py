import random

# 1. 상자 생성과 섞기
# 1번 팀원 코드
def create_boxes():
    boxes = list(range(1, 101))  # 100개의 상자 생성
    random.shuffle(boxes)  # 무작위로 섞기
    return boxes
