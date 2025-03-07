-- There is a queue of people waiting to board a bus. However, the bus has a weight limit of 1000 kilograms,
-- so there may be some people who cannot board.
-- Write a solution to find the person_name of the last person that can fit on the bus without exceeding the weight limit.
-- The test cases are generated such that the first person does not exceed the weight limit.

with sum_cte as (
    select
    person_name,
    weight,
    turn,
    sum(weight) over (order by turn) sum
    from Queue
    order by turn
)

select Queue.person_name
from
(
select max(turn) max_turn
from sum_cte
where sum <= 1000
) a
inner join Queue on a.max_turn = Queue.turn
