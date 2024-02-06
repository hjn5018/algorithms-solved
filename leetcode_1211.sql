-- We define query quality as:
-- The average of the ratio between query rating and its position.
-- We also define poor query percentage as:
-- The percentage of all queries with rating less than 3.
-- Write a solution to find each query_name, the quality and poor_query_percentage.
-- Both quality and poor_query_percentage should be rounded to 2 decimal places.

select query_name,
       round(sum(rating / position) / count(query_name), 2) quality,
       round(sum(rating < 3) / count(query_name) * 100, 2) poor_query_percentage
from Queries
where query_name is not null
group by query_name
