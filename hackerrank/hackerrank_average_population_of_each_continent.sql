-- select * from city
-- select * from country

-- select country.continent, round(avg(city.population))
-- from city
-- left join country
-- on city.countrycode = country.code

-- select country.continent, round(avg(city.population))
-- from city
-- left join country
-- on city.countrycode = country.code
-- group by country.continent
-- Asia 693038
-- Europe 175138
-- NULL 266867
-- Oceania 109190
-- South America 147435
-- Africa 274439


-- select country.continent, round(avg(city.population))
-- from city
-- left join country
-- on city.countrycode = country.code
-- group by country.continent
-- where country.continent is not Null
-- ERROR 1064 (42000) at line 9: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'where country.continent is not Null' at line 6

-- select country.continent, round(avg(city.population))
-- from city
-- left join country
-- on city.countrycode = country.code
-- group by country.continent
-- where country.continent is not NULL
-- ERROR 1064 (42000) at line 30: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'where country.continent is not NULL' at line 6

-- select c.continent, round(avg(city.population))
-- from city
-- left join
-- (
-- select *
-- from country
-- where continent is not null
-- ) c
-- on city.countrycode = c.code
-- group by c.continent
-- Asia 693038
-- Europe 175138
-- NULL 266867
-- Oceania 109190
-- South America 147435
-- Africa 274439

-- select c.continent, round(avg(a.population))
-- from
-- (
-- select *
-- from city
-- where city.countrycode is not null
-- ) a
-- left join
-- (
-- select *
-- from country
-- where continent is not null
-- ) c
-- on city.countrycode = c.code
-- group by c.continent

-- 아직 못 품
select country.continent, floor(avg(city.population))
from country
inner join city
on city.countrycode = country.code
group by 1
