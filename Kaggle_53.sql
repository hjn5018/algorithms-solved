-- ONLINE_SALE 테이블에서 동일한 회원이 동일한 상품을 재구매한 데이터를 구하여, 재구매한 회원 ID와 재구매한 상품 ID를 출력하는 SQL문을 작성해주세요. 결과는 회원 ID를 기준으로 오름차순 정렬해주시고 회원 ID가 같다면 상품 ID를 기준으로 내림차순 정렬해주세요.

select user_id, product_id
from
(
select user_id, product_id, count(product_id) cnt
from online_sale
group by user_id, product_id
) a
where cnt >= 2
order by 1, 2 desc

-- group by를 하나의 컬럼이 아닌 두개의 컬럼으로 설정하여 count할 수 있음