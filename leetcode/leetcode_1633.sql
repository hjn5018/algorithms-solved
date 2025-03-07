-- Write a solution to find the percentage of the users registered in each contest rounded to two decimals.
-- Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.

select a.contest_id, round((cnt_a / cnt_b * 100), 2) percentage
from 
(
select contest_id, count(user_id) cnt_a
from Register
group by contest_id
) a join
(
select count(1) cnt_b
from Users
) b
order by percentage desc, a.contest_id