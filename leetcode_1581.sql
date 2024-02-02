# Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.

select b.no_trans customer_id, count(b.no_trans)count_no_trans
from
(
select if(a.visit_id is null, customer_id, null) no_trans
from Visits v left join
(
select distinct visit_id
from Transactions
) a on v.visit_id = a.visit_id
) b
where b.no_trans is not null
group by b.no_trans
