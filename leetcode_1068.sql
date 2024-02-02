-- Write a solution to report the product_name, year, and price for each sale_id in the Sales table.

select product_name, year, price
from Sales join Product using(product_id)
