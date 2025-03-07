-- round(count(lat_n)/2)
-- # 250

-- select lat_n
-- from station
-- order by lat_n
-- limit round(count(lat_n)/2)

-- ERROR 1064 (42000) at line 3: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(count(lat_n)/2)' at line 4
--

select round(max(a1.lat_n), 4)
from
(
select lat_n
from station
order by lat_n
limit 250
) a1
