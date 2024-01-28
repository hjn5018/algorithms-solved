-- USED_GOODS_BOARD와 USED_GOODS_USER 테이블에서 완료된 중고 거래의 총금액이 70만 원 이상인 사람의 회원 ID, 닉네임, 총거래금액을 조회하는 SQL문을 작성해주세요. 결과는 총거래금액을 기준으로 오름차순 정렬해주세요.

select *
from
(
SELECT writer_id, nickname, sum(price) sum_price
from used_goods_board b left join used_goods_user u on b.writer_id = u.user_id
where status = 'done'
group by writer_id
order by 2 desc
) a
where sum_price >= '700000'