-- USER_INFO 테이블과 ONLINE_SALE 테이블에서 년, 월, 성별 별로 상품을 구매한 회원수를 집계하는 SQL문을 작성해주세요. 결과는 년, 월, 성별을 기준으로 오름차순 정렬해주세요. 이때, 성별 정보가 없는 경우 결과에서 제외해주세요.

SELECT date_format(date(sales_date), '%Y') YEAR, date_format(date(sales_date), '%m') MONTH, GENDER, count(distinct i.user_id) USERS
from user_info i left join online_sale o on i.user_id = o.user_id
where gender is not null and sales_date is not null
group by 1,2,3
order by 1,2,3

-- count안에도 distinct를 사용할 수 있다.