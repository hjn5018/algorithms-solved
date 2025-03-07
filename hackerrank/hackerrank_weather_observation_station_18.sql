-- with
-- cte1 as (select max(LAT_N) from STATION)
-- select * from cte1
-- 144.98906270

-- select max(LAT_N) from STATION
-- 144.98906270

-- with
-- cte1 as (select max(LAT_N) from STATION),
-- cte2 as (select max(LONG_W) from STATION)
-- select * from cte1 join cte2
-- 144.98906270 164.87604770

-- with
-- cte1 as (select max(LAT_N) from STATION),
-- cte2 as (select max(LONG_W) from STATION),
-- cte3 as (select min(LAT_N) from STATION),
-- cte4 as (select min(LONG_W) from STATION)
-- select * from cte1 join cte2
-- union
-- select * from cte3 join cte4
-- 144.98906270 164.87604770
-- 25.07352606 25.10565434

-- with
-- cte1 as (select max(LAT_N) from STATION),
-- cte2 as (select max(LONG_W) from STATION),
-- cte3 as (select min(LAT_N) from STATION),
-- cte4 as (select min(LONG_W) from STATION)
-- select 1 from cte1
-- 1

-- with
-- cte1 as (select max(LAT_N) from STATION),
-- cte2 as (select max(LONG_W) from STATION),
-- cte3 as (select min(LAT_N) from STATION),
-- cte4 as (select min(LONG_W) from STATION)
-- select max(LAT_N) from cte1
-- ERROR 1054 (42S22) at line 34: Unknown column 'LAT_N' in 'field list'

with
cte1 as (select max(LAT_N) from STATION),
cte2 as (select max(LONG_W) from STATION),
cte3 as (select min(LAT_N) from STATION),
cte4 as (select min(LONG_W) from STATION)
select max(LAT_N) from cte1
-- 아직 못 품..
