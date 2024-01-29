-- 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회하는 SQL 문을 작성해주세요.

select flavor
from
(
select h.total_order + a.sum_t_o, h.flavor
from first_half h left join
(
SELECT flavor, sum(total_order) sum_t_o
from july j
group by flavor
) a on h.flavor = a.flavor
order by 1 desc
limit 3
) b