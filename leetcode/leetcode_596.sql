-- Write a solution to find all the classes that have at least five students.

select class
from Courses
group by class
having count(class) >= 5