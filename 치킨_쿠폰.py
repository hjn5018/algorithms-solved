def solution(chicken):
    # Initial coupon = paid_chicken
    coupon = chicken
    service_chicken = 0
    sum_service_chicken = 0
    
    while True:
        # If coupon is enough,
        if coupon >= 10:
            # order service_chicken
            service_chicken += coupon//10
            # and give coupon,
            coupon = coupon % 10
            # take coupon
            coupon += service_chicken
            sum_service_chicken += service_chicken
            service_chicken = 0
        else:
            break
    
    return sum_service_chicken
    
        
# 추론 과정
#     치킨 1081마리
#     쿠폰 1081개
    
#     쿠폰 1080개 소진 1개 남음
#     108마리 주문 쿠폰 108+1개 남음
#     10마리 주문 쿠폰 8+1+1개
    
#     max_service_chiken = x
#     remain_coupon = y
    
#     chicken//10
#     remain_coupon = chicken%10
    
#     while True:
#         if chicken > 10:
            
    #3 https://school.programmers.co.kr/learn/courses/30/lessons/120884
