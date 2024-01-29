-- 데이터 분석 팀에서는 우유(Milk)와 요거트(Yogurt)를 동시에 구입한 장바구니가 있는지 알아보려 합니다. 우유와 요거트를 동시에 구입한 장바구니의 아이디를 조회하는 SQL 문을 작성해주세요. 이때 결과는 장바구니의 아이디 순으로 나와야 합니다.

select cart_id
from
(
select distinct p.cart_id cart_id, p.name p_n, a.name a_n
from cart_products p inner join
(
SELECT id, cart_id, name
from cart_products
where name = 'milk'
) a on p.cart_id = a.cart_id
where p.name = 'yogurt'
) b
order by 1