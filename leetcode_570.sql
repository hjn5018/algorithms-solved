# Write a solution to find managers with at least five direct reports.

select e.name
from Employee e join
(
select managerID
from Employee
where managerID is not null
group by managerID
having count(managerID) >= 5
) a
where e.id = a.managerID