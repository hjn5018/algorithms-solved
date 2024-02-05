-- Write an SQL query that reports the average experience years of all the employees for each project, rounded to 2 digits.

select p.project_id, round((sum(e.experience_years) / count(e.employee_id)), 2) average_years
from Project p left join Employee e
using(employee_id)
where e.experience_years is not null
group by p.project_id