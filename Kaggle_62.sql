-- CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 대여 시작일이 2022년 9월에 속하는 대여 기록에 대해서 대여 기간이 30일 이상이면 '장기 대여' 그렇지 않으면 '단기 대여' 로 표시하는 컬럼(컬럼명: RENT_TYPE)을 추가하여 대여기록을 출력하는 SQL문을 작성해주세요. 결과는 대여 기록 ID를 기준으로 내림차순 정렬해주세요.

SELECT HISTORY_ID, CAR_ID, date_format(date(start_date), '%Y-%m-%d') START_DATE, date_format(date(end_date), '%Y-%m-%d') END_DATE, if(datediff(end_date, start_date) >= 29, "장기 대여", "단기 대여") RENT_TYPE
from car_rental_company_rental_history
where date_format(date(start_date), '%Y-%m') like '2022-09%'
order by 1 desc


-- 문제의 예시에서 history_id 컬럼의 데이터가 1인 값을 살펴보면, datediff가 29이다. 엄밀히 하자면 
-- datediff(end_date, start_date)+1 >= 30
-- 대여 당일에 반납을 해도 1일 대여로 한다.