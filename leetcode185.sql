-- A company's executives are interested in seeing who earns the most money in each of the company's departments.
-- A high earner in a department is an employee who has a salary in the top three unique salaries for that department.
-- Write a solution to find the employees who are high earners in each of the departments.

with cte as (
    select d.name Department,
           e.name Employee,
           e.salary Salary,
           dense_rank()over(partition by e.departmentId order by e.salary desc) rnk
    from Employee e
    join Department d
    on e.departmentId = d.id
)

select Department,
       Employee,
       Salary
from cte
where rnk <= 3
