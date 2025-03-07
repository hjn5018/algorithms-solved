-- Write a solution to:
-- Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
-- Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.

with cte as (
    select u.name, m.title, r.rating, r.created_at
    from MovieRating r
    left join Movies m
    on r.movie_id = m.movie_id
    left join Users u
    on r.user_id = u.user_id
)

select a.name results
from
(
select name, count(1) cnt
from cte
group by name
order by cnt desc, name
limit 1
) a

union all

select b.title results
from
(
select title, avg(rating) avg_rt
from cte
where created_at like ('%2020-02%')
group by title
order by avg_rt desc, title
limit 1
) b
