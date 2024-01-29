-- 이 서비스에서는 공간을 둘 이상 등록한 사람을 "헤비 유저"라고 부릅니다. 헤비 유저가 등록한 공간의 정보를 아이디 순으로 조회하는 SQL문을 작성해주세요.

select id, name, p.host_id
from places p inner join
(
select *
from
(
select host_id, count(1) cnt
from places
group by host_id
) a
where cnt >= 2
)b on p.host_id = b.host_id
order by id