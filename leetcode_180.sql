-- Find all numbers that appear at least three times consecutively.

select distinct L1.num ConsecutiveNums
from Logs L1, Logs L2, Logs L3
where L1.id + 1 = L2.id
and L2.id + 1 = L3.id
and L1.num = L2.num
and L2.num = L3.num
