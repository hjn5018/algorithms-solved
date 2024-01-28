-- FOOD_PRODUCT와 FOOD_ORDER 테이블에서 생산일자가 2022년 5월인 식품들의 식품 ID, 식품 이름, 총매출을 조회하는 SQL문을 작성해주세요. 이때 결과는 총매출을 기준으로 내림차순 정렬해주시고 총매출이 같다면 식품 ID를 기준으로 오름차순 정렬해주세요.

select product_id, product_name, sum(total_sales)
from
(
SELECT p.product_id, product_name, price*amount total_sales
from food_product p left join food_order o on p.product_id = o.product_id
where substr(produce_date, 6, 2) = 05
) a
group by product_name
order by 3 desc, 1