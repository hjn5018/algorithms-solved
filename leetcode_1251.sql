# Write a solution to find the average selling price for each product. average_price should be rounded to 2 decimal places.

select p.product_id, round(sum(u.units * price) / sum(units), 2) average_price
from Prices p join UnitsSold u on p.product_id = u.product_id
where u.purchase_date between p.start_date and p.end_date
group by p.product_id
