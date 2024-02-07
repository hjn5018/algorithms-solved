-- For this problem, we will consider a manager an employee who has at least 1 other employee reporting to them.
-- Write a solution to report the ids and the names of all managers,
-- the number of employees who report directly to them,
-- and the average age of the reports rounded to the nearest integer
-- Return the result table ordered by employee_id.

select a.employee_id, a.name, b.reports_count, b. average_age
from
(
select employee_id, name
from Employees
where employee_id in
(select reports_to
from Employees)
) a join
(
select reports_to, count(1) reports_count, round(sum(age)/count(1)) average_age
from Employees
where reports_to is not null
group by reports_to
) b on a.employee_id = b.reports_to
order by a.employee_id