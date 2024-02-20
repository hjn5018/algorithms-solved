-- Write a solution to get the names of products that have at least 100 units ordered in February 2020 and their amount.
-- Return the result table in any order.

select P.product_name,
       sum(O.unit) unit
from Orders O
right join Products P
on P.product_id = O.product_id
where order_date like '%2020-02%'
group by P.product_name
having sum(O.unit) >= 100
