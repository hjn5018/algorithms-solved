-- Write a solution to select the product id, year, quantity, and price for the first year of every product sold.

select product_id, a.first_year, quantity, price
from Sales left join
(
select product_id p_id, min(year) first_year
from Sales
group by product_id
) a on product_id = a.p_id
where year = a.first_year