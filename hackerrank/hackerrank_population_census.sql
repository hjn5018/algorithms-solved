-- select * from CITY

-- select sum(POPULATION) from COUNTRY where CONTINENT = 'Asia'

-- select *
-- from COUNTRY left join CITY
-- where CONTINENT = 'Asia'
-- check the manual that corresponds to your MySQL server version for the right syntax to use near 'where CONTINENT = 'Asia'' at line 3

-- select *
-- from COUNTRY join CITY
-- where CONTINENT = 'Asia'

select sum(CITY.POPULATION)
from CITY
left join COUNTRY
on CITY.COUNTRYCODE = COUNTRY.CODE
where CONTINENT = 'Asia'
