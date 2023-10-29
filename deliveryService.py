# 클래스 자율과제 >> 편의점 반값 택배 접수

import random
from datetime import date
import datetime


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
        
        res_num = random.randint(0,9999999999999) # 예약번호(13자리)
        deli_num = random.randint(0,999999999999) # 운송장번호(12자리)
        
        # 예약번호, 운송장번호 자릿수 설정
        self.res_num = str(res_num).zfill(13)
        self.deli_num = str(deli_num).zfill(12)
        
        # 기본 배송료 초기화
        self.deli_fee = 0
        
        # 접수 날짜 표시(yyyy-mm-dd)
        # self.day = datetime.datetime.now()      >> 시간까지 출력됨
        today = date.today()                    # >> 오늘 날짜 반환
        self.resDay = date(today.year, today.month, 26)  # >> 접수 날짜: 2023-10-26
        

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
    # def statusCheck(self, today):
    #     # 3일 이상          -> 고객 전달
    #     # 1일 이상, 3일 미만 -> 배송 중
    #     # 1일 미만         -> 배송 대기 중
    #     # today = date.today()  >>오늘 날짜 리턴
        
    #     condition = abs(today - self.resDay)
    #     if condition >= 3:
    #         # print(f'구분: 반값택배\t접수일자: {self.day}\t운송장번호: {self.deli_num}\t상태: 고객전달')
    #         print("상태: 고객전달")
    #     elif 1 <= condition < 3:
    #         print("상태: 배송 중")
    #     else:
    #         print("배송 대기 중")
            


# 택배 접수 확인
delivery_1 = Delivery('Kiki', '010-5678-5678', '서울특별시', '핸드폰')

print(f'보내는 사람: {delivery_1.f_name}\n')

print(f'받는 사람: {delivery_1.t_name}')
print(f'받는 사람 전화번호: {delivery_1.t_phoneNum}')
print(f'받는 사람 주소: {delivery_1.t_address}\n')

print(f'예약 번호: {delivery_1.res_num}')
print(f'운송장번호: {delivery_1.deli_num}')
print(f'접수 시간: {delivery_1.resDay}\n')

print(f'배송료: {delivery_1.checkWeight(0.25)}\n')

print(f'예약 번호: {delivery_1.reserveNumCheck(delivery_1.res_num)}\n')

print(f'운송장 번호 조회: {delivery_1.deliveryNumCheck(delivery_1.deli_num)}\n')

# delivery_1.statusCheck(date.today())







