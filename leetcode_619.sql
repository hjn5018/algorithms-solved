-- A single number is a number that appeared only once in the MyNumbers table.
-- Find the largest single number. If there is no single number, report null.

select max(a.num) num
from
(
select N.num
from MyNumbers M left join myNumbers N on M.num = N.num
group by M.num
having count(N.num) < 2
) a