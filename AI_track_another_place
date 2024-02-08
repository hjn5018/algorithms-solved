-- Write a solution to report all the employees with their primary department. For employees who belong to one department, report their only department.

select employee_id, department_id
from Employee
group by employee_id
having count(primary_flag) = 1

union

select employee_id, department_id
from Employee
where primary_flag = 'Y'
