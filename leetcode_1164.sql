-- Write a solution to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.

with recent_prices as (
    select
    product_id,
    new_price,
    row_number() over(partition by product_id order by change_date desc) rn
    from products
    where
    change_date <= 20190816
),
product_list as (
    select
    distinct product_id
    from products
)

select
pl.product_id,
ifnull(rp.new_price, 10) price
from product_list pl
left join
recent_prices rp on pl.product_id = rp.product_id and rp.rn = 1
