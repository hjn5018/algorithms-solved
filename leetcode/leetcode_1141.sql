-- Write a solution to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively. A user was active on someday if they made at least one activity on that day.

select activity_date day, count(distinct user_id) active_users
from Activity
where activity_date between 20190628 and 20190727
group by activity_date