-- 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

with recursive cte as(
 select 0 as num
 union all
 select num + 1 from cte
 where num < 23
)
select num, ifnull(cnt, 0)
from cte left join
(
SELECT Hour(datetime) h, count(1) cnt
from animal_outs
group by 1
) a on cte.num = a.h