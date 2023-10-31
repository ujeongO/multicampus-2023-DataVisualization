# 클래스 자율과제 >> 편의점 반값 택배 접수

import random
# import datetime
# from datetime import timedelta
from datetime import datetime


# 택배 접수 클래스 생성
class Delivery:
    # 생성자 >> 택배 접수
    def __init__(self, t_name, t_phoneNum, t_address, name):
        self.f_name = '오유정'
        self.f_phoneNum = '010-1234-1234'
        self.f_address = '광주광역시'
        self.t_name = t_name
        self.t_phoneNum = t_phoneNum
        self.t_address = t_address
        self.name = name            # 물품명
        
        # print(f'{self.name} 물품이 접수되었습니다.')
        
        # 예약번호, 운송장번호
        res_num = random.randint(0,9999999999999) # 예약번호(13자리)
        deli_num = random.randint(0,999999999999) # 운송장번호(12자리)
        
        # 예약번호, 운송장번호 자릿수 설정
        self.res_num = str(res_num).zfill(13)
        self.deli_num = str(deli_num).zfill(12)
        
        # 기본 배송료 초기화
        self.deli_fee = 0
        
        # 접수 날짜 표시(yyyy-mm-dd)
        # self.resDay = datetime.today()
        # self.resDay = datetime(2023, 10, 13, 21, 40, 5)
        self.resDay = datetime(2023, 10, 30)    # >> 접수 날짜 2023-10-30 고정
        

    # 무게에 따른 배송료 계산
    def checkWeight(self, weight):
        # 5kg 초과 -> 0 원(배송 불가)
        # 1~5kg   -> 2,200 원
        # 1kg 미만 -> 1,800 원
      
        if weight < 1:
            self.deli_fee = 1800
            print(f"{weight}kg 입니다. 배송료는 {self.deli_fee} 원 입니다.")
        elif 1 <= weight <= 5:
            self.deli_fee = 2200
            print(f"{weight}kg 입니다. 배송료는 {self.deli_fee} 원 입니다.")
        else:
            self.deli_fee = 0
            print("5kg 초과하였으므로 접수할 수 없습니다. 일반 택배로 접수해주세요.")
      
        return self.deli_fee
    
    # 예약 번호 조회
    def reserveNumCheck(self, num):
        if num == self.res_num:
            print(f'{self.name}\n')
            print(f'{self.resDay}\n예약번호: {self.res_num}\t운송장출력: {self.deli_num}')
        else:
            print("예약 내역이 없습니다.")
            num = '-'
            
        return num
         
    # 운송장번호 조회
    def deliveryNumCheck(self, num):
        if num == self.deli_num:
            print(f'{self.resDay}\n보내는 분: {self.f_name}\n받는 분: {self.t_name}\n상품명: {self.name}')
        else:
            num = '-'
            print("해당 운송장의 배송정보를 조회할 수 없습니다.\n운송장 번호를 확인해주세요.")
        return num
    
    # 배송 현황 조회
    def statusCheck(self, today):
        # 날짜 차이(조회 날짜 - 접수 날짜) 계산
        # 3일 이상             -> 고객 전달
        # 1일 이상, 3일 미만    -> 배송 중
        # 1일 미만            -> 배송 대기 중
        
        # 접수 날짜
        # self.resDay = datetime(2023, 10, 28)
        
        condition = today - self.resDay
        
        if condition.days >= 3:
            print(f'{condition.days}일 소요. 고객 전달')
        elif 1 <= condition.days:
            print(f'{condition.days}일 소요. 배송 중')
        else:
            print(f'{condition.days}일 소요. 배송 대기 중')
        
        return condition.days
            

# GS25
class GS25(Delivery):
    def __init__(self, t_name, t_phoneNum, t_address, name, weight, resDay):
        super().__init__(t_name, t_phoneNum, t_address, name)
        self.weight = weight
        self.resDay = resDay
        self.storeName = 'GS25'
        
        print(f'{self.storeName} 에서 {self.resDay} 에 {self.name} 물품을 접수했습니다.')
        
    # 무게 
    def checkWeight(self):
        super().checkWeight(self.weight)
        
    # 배송 현황 조회
    def deliCheck(self, today):
        super().statusCheck(today)
        
    

# CU
class CU(Delivery):
    def __init__(self, t_name, t_phoneNum, t_address, name, weight, resDay):
        super().__init__(t_name, t_phoneNum, t_address, name)
        self.weight = weight
        self.resDay = resDay
        self.storeName = 'CU'
        
        print(f'{self.storeName} 에서 {self.resDay} 에 {self.name} 물품을 접수하였습니다.')
    
    # 무게 
    def checkWeight(self):
        super().checkWeight(self.weight)
        
    # 배송 현황 조회
    def deliCheck(self, today):
        super().statusCheck(today)
        
        

# 택배 접수 확인
delivery_1 = Delivery('Kiki', '010-5678-5678', '서울특별시', '핸드폰')

print(f'보내는 사람: {delivery_1.f_name}\n')

print(f'받는 사람: {delivery_1.t_name}')
print(f'받는 사람 전화번호: {delivery_1.t_phoneNum}')
print(f'받는 사람 주소: {delivery_1.t_address}\n')

print(f'예약 번호: {delivery_1.res_num}')
print(f'운송장번호: {delivery_1.deli_num}')
print(f'접수 시간: {delivery_1.resDay}\n')
# print(f'접수 시간: {delivery_1.day}\n')

print(f'배송료: {delivery_1.checkWeight(0.25)}\n')

print(f'예약 번호: {delivery_1.reserveNumCheck(delivery_1.res_num)}\n')

print(f'운송장 번호 조회: {delivery_1.deliveryNumCheck(delivery_1.deli_num)}\n')

# 현재 날짜, 시간
# print(datetime.now())
delivery_1.statusCheck(datetime.now())

print()
gs = GS25('몽몽', '010-1111-1111', '서울', '컵', 2, datetime(2023, 10, 29))
gs.checkWeight()
gs.deliCheck(datetime.now())

print()

cu = CU('Koko', '010-1234-5678', '서울', '책', 0.3, datetime(2023, 10, 31))
cu.checkWeight()
cu.deliCheck(datetime.now())


