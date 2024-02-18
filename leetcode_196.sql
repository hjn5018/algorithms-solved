-- Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
-- For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.

delete p1
from Person p1, person p2
where p1.email = p2.email
and p1.id > p2.id
