-- Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

with cte as (
    select *,
           dense_rank() over(order by salary desc) rnk
    from Employee
)

select min(salary) SecondHighestSalary
from cte
where rnk = 2
