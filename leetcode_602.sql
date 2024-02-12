-- Write a solution to find the people who have the most friends and the most friends number.
-- The test cases are generated so that only one person has the most friends.

with cte as (
    select requester_id as id
    from RequestAccepted
    union all
    select accepter_id as id
    from RequestAccepted
)

select id, count(id) as num
from cte
group by id
order by count(id) desc
limit 1
