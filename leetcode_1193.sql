-- Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of approved transactions and their total amount.

select date_format(trans_date, '%Y-%m') month,
       country,
       count(1) trans_count,
       sum(if(state = 'approved', 1, 0)) approved_count,
       sum(amount) trans_total_amount,
       sum(if(state = 'declined', amount = 0, amount)) approved_total_amount
from Transactions
group by date_format(trans_date, '%Y-%m'), country
