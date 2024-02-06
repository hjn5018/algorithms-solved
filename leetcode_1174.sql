-- If the customer's preferred delivery date is the same as the order date, then the order is called immediate; otherwise, it is called scheduled.
-- The first order of a customer is the order with the earliest order date that the customer made. It is guaranteed that a customer has precisely one first order.
-- Write a solution to find the percentage of immediate orders in the first orders of all customers, rounded to 2 decimal places.

select round((sum(im_or_sc) / count(1))*100, 2) immediate_percentage
from
(
select if(b.first_order = b.min_cpdd, 1, 0) im_or_sc 
from
(
select a.customer_id, a.first_order, min(d.customer_pref_delivery_date) min_cpdd
from Delivery d
left join
(
select customer_id, min(order_date) first_order
from Delivery
group by customer_id
) a
on d.customer_id = a.customer_id
group by a.customer_id
order by d.customer_id, d.order_date
) b
) c