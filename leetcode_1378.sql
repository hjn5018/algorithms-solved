# Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.

select unique_id, name
from employees e left join employeeuni u on e.id = u.id