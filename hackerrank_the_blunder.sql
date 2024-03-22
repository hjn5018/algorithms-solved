-- select avg(Salary)- regex('[1-9]') from EMPLOYEES 
-- select salary regexp ('^2') from EMPLOYEES
-- select salary from EMPLOYEES where salary regexp('^2')
-- select salary from employees
-- select round(avg(Salary) - avg(regexp_replace(Salary, 0, '')))  from EMPLOYEES
-- select ceil(2.4)
select ceil(avg(Salary) - avg(regexp_replace(Salary, 0, '')))  from EMPLOYEES
