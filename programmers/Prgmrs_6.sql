-- shout out to 이주용

select name, count_name
from
(
select NAME,
    count(NAME) as count_name
from ANIMAL_INS 
group by NAME
) a
where count_name > 1
order by name