-- PRODUCT 테이블에서 만원 단위의 가격대 별로 상품 개수를 출력하는 SQL 문을 작성해주세요. 이때 컬럼명은 각각 컬럼명은 PRICE_GROUP, PRODUCTS로 지정해주시고 가격대 정보는 각 구간의 최소금액(10,000원 이상 ~ 20,000 미만인 구간인 경우 10,000)으로 표시해주세요. 결과는 가격대를 기준으로 오름차순 정렬해주세요.

SELECT case when price >= 10000 and price < 20000 then 10000
            when price >= 20000 and price < 30000 then 20000
            when price >= 30000 and price < 40000 then 30000
            when price >= 40000 and price < 50000 then 40000
            when price >= 50000 and price < 60000 then 50000
            when price >= 60000 and price < 70000 then 60000
            when price >= 70000 and price < 80000 then 70000
            when price >= 80000 and price < 90000 then 80000
            end price_group,
            count(1) products
from product
group by price_group
order by price_group