
print('================================')
name=input("가게 이름을 입력하세요.: ")
print("각 달의 총매출을 입력하세요.")
print("금액을 입력할 땐 '원'과 ','를 제외하고 숫자만 입력해 주세요.")
jan = int(input("1월 총매출: "))
feb = int(input("2월 총매출: "))
mar = int(input("3월 총매출: "))
apr = int(input("4월 총매출: "))
may = int(input("5월 총매출: "))
jun = int(input("6월 총매출: "))
jul = int(input("7월 총매출: "))
aug = int(input("8월 총매출: "))
sep = int(input("9월 총매출: "))
octo = int(input("10월 총매출: "))
nov = int(input("11월 총매출: "))
dec = int(input("12월 총매출: "))

data=[jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec]

total = jan+feb+mar+apr+may+jun+jul+aug+sep+octo+nov+dec
average = total / 12
print('================================')
print("올해의 총 매출은", total,"원 입니다.")

print('================================')
print("가게의 지출을 입력하는 구간입니다.")
print("금액을 입력할 때 '원'을 빼고 입력해주세요.")

month = 0
sum = 0

while month <12 :
    
    month += 1
    mon_total = 0
  
    print(month,'월의 인건비, 월세, 관리비, 재료비를 입력하세요!')
    mon_total += int(input('인건비(4대 보험 포함): '))
    mon_total += int(input('월세: '))
    mon_total += int(input('관리비(가스비 포함): '))
    mon_total += int(input('재료비: '))
  
    print(month, '월 총 지출은',mon_total,'원 입니다.')
    print()

    sum += mon_total
    m_average=sum/12
print('올해의 총 지출',sum,'원 입니다.')
    
print()
print("=========================")
print("가게 이름: ", name)
print("총 매출 결과")
print("올해 최고 매출은", max(data),"원 입니다.")
print("올해 최저 매출은", min(data), "원 입니다.")
print("총 매출의 평균: %.2f" % average,"원 입니다.")
print("총 지출의 평균: %.2f" % m_average, "원 입니다.")
print("1월부터 12월 까지의 순수 이익은", total-sum,"원 입니다.")
print("=========================")

