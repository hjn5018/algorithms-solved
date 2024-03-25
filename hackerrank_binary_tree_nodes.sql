-- select *
-- from bst
-- 1 2
-- 3 2
-- 5 6
-- 7 6
-- 2 4
-- 6 4
-- 4 15
-- 8 9
-- 10 9
-- 12 13
-- 14 13
-- 9 11
-- 13 11
-- 11 15
-- 15 NULL

-- select *
-- from bst
-- left join bst b
-- on bst.p = b.n
-- 1 2 2 4
-- 3 2 2 4
-- 5 6 6 4
-- 7 6 6 4
-- 2 4 4 15
-- 6 4 4 15
-- 4 15 15 NULL
-- 8 9 9 11
-- 10 9 9 11
-- 12 13 13 11
-- 14 13 13 11
-- 9 11 11 15
-- 13 11 11 15
-- 11 15 15 NULL
-- 15 NULL NULL NULL

select distinct(bst.n),
case when bst.p is null then Root,
    when ...
from bst
left join bst b
on bst.p = b.n
order by 1

조인했을 때 중간에 놓여있지 않은 값은 leaf이고, null이 붙어있는 값은 root이고 나머지는 inner인데,
이걸 어떻게 나타내나..
