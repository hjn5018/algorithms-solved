-- CAR_RENTAL_COMPANY_CAR 테이블과 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블과 CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블에서 자동차 종류가 '세단' 또는 'SUV' 인 자동차 중 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력하는 SQL문을 작성해주세요. 결과는 대여 금액을 기준으로 내림차순 정렬하고, 대여 금액이 같은 경우 자동차 종류를 기준으로 오름차순 정렬, 자동차 종류까지 같은 경우 자동차 ID를 기준으로 내림차순 정렬해주세요.

select car_id, c.car_type, round(daily_fee*30*(1-0.01*discount_rate)) fee
from CAR_RENTAL_COMPANY_CAR c join CAR_RENTAL_COMPANY_DISCOUNT_PLAN using(car_type)
where car_type in ('세단', 'suv') and car_id not in
(select distinct car_id
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where start_date <= 20221130 and end_date >= 20221101)
and duration_type like '%30%'
having fee >= 500000 and fee < 2000000
order by 3 desc, 2, 1 desc
밑으로 시행착오ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
-- CAR_RENTAL_COMPANY_CAR 테이블과 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블과 CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블에서 자동차 종류가 '세단' 또는 'SUV' 인 자동차 중 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력하는 SQL문을 작성해주세요. 결과는 대여 금액을 기준으로 내림차순 정렬하고, 대여 금액이 같은 경우 자동차 종류를 기준으로 오름차순 정렬, 자동차 종류까지 같은 경우 자동차 ID를 기준으로 내림차순 정렬해주세요.

select car_id, c.car_type, round(daily_fee*30*(1-0.01*discount_rate)) FEE
from
(
select car_id, car_type, daily_fee
from CAR_RENTAL_COMPANY_CAR
where car_type = '세단' or car_type = 'suv' and car_id not in
(select distinct car_id
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where end_date >= 20221101 and start_date <= 20221130)
) c left join
(
select car_type, discount_rate
from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
where duration_type = '30일 이상' and car_type in ('세단', 'SUV')
) d on c.car_type = d.car_type
where daily_fee*30*(1-0.01*discount_rate) >= 500000 and
      daily_fee*30*(1-0.01*discount_rate) < 2000000
order by 3 desc, 2, 1 desc

ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

-- CAR_RENTAL_COMPANY_CAR 테이블과 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블과 CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블에서 자동차 종류가 '세단' 또는 'SUV' 인 자동차 중 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력하는 SQL문을 작성해주세요. 결과는 대여 금액을 기준으로 내림차순 정렬하고, 대여 금액이 같은 경우 자동차 종류를 기준으로 오름차순 정렬, 자동차 종류까지 같은 경우 자동차 ID를 기준으로 내림차순 정렬해주세요.

select car_id, d.car_type, floor(daily_fee*(1-discount_rate*0.01)*30) FEE
from
(
select distinct car_id, car_type, daily_fee
from
(
SELECT c.car_id, car_type, daily_fee
from CAR_RENTAL_COMPANY_CAR c inner join
(
select *
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where end_date < 20221101 or start_date > 20221130
) h on c.car_id = h.car_id
where car_type in ('세단', 'suv')
) a 
) b left join 
(
select car_type, discount_rate
from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
where duration_type like '30%'
) d on b.car_type = d.car_type
where floor(daily_fee*(1-discount_rate*0.01)*30) >= 500000 and 
      floor(daily_fee*(1-discount_rate*0.01)*30) < 2000000
order by 3 desc, 2, 1 desc

-- CAR_RENTAL_COMPANY_CAR 테이블과 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블과 CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블에서 자동차 종류가 '세단' 또는 'SUV' 인 자동차 중 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력하는 SQL문을 작성해주세요. 결과는 대여 금액을 기준으로 내림차순 정렬하고, 대여 금액이 같은 경우 자동차 종류를 기준으로 오름차순 정렬, 자동차 종류까지 같은 경우 자동차 ID를 기준으로 내림차순 정렬해주세요.

select car_id CAR_ID, c.car_type CAR_TYPE, round(daily_fee*30*(1-0.01*discount_rate)) FEE
from
(
select a.car_id, car_type, daily_fee
from
(
select car_id, car_type, daily_fee
from CAR_RENTAL_COMPANY_CAR
where car_type = '세단' or car_type = 'suv'
) a inner join
(
select distinct car_id
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where end_date < 20221101 or start_date > 20221130
) b on a.car_id = b.car_id
) c left join
(
select car_type, discount_rate
from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
where duration_type = '30일 이상' and car_type in ('세단', 'SUV')
) d on c.car_type = d.car_type
where (daily_fee*30*(1-0.01*discount_rate)) >= 500000 and
      (daily_fee*30*(1-0.01*discount_rate)) < 2000000
order by 3 desc, 2, 1 desc


-- CAR_RENTAL_COMPANY_CAR 테이블과 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블과 CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블에서 자동차 종류가 '세단' 또는 'SUV' 인 자동차 중 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력하는 SQL문을 작성해주세요. 결과는 대여 금액을 기준으로 내림차순 정렬하고, 대여 금액이 같은 경우 자동차 종류를 기준으로 오름차순 정렬, 자동차 종류까지 같은 경우 자동차 ID를 기준으로 내림차순 정렬해주세요.

select car_id, car_type, round(daily_fee*30*(1-0.01*discount_rate)) FEE
from CAR_RENTAL_COMPANY_CAR join CAR_RENTAL_COMPANY_DISCOUNT_PLAN using(car_type)
where car_type in ('세단', 'suv')
      and car_id in (select car_id
                     from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                     where end_date < 20221101 or
                           start_date > 20221130)
      and duration_type like '%30%'
having fee >= 500000 and fee < 2000000
order by 3 desc, 2, 1 desc

ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
select car_id
from CAR_RENTAL_COMPANY_CAR
where car_id not in
(select distinct car_id
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where end_date >= 20221101 and start_date <= 20221130)
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
-- CAR_RENTAL_COMPANY_CAR 테이블과 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블과 CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블에서 자동차 종류가 '세단' 또는 'SUV' 인 자동차 중 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서 자동차 ID, 자동차 종류, 대여 금액(컬럼명: FEE) 리스트를 출력하는 SQL문을 작성해주세요. 결과는 대여 금액을 기준으로 내림차순 정렬하고, 대여 금액이 같은 경우 자동차 종류를 기준으로 오름차순 정렬, 자동차 종류까지 같은 경우 자동차 ID를 기준으로 내림차순 정렬해주세요.

select *
from CAR_RENTAL_COMPANY_CAR
where car_type in ('세단', 'suv') and car_id not in
(select distinct car_id
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where start_date <= 20221130 and end_date >= 20221101)
