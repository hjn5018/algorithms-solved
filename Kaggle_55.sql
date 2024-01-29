-- USED_GOODS_BOARD와 USED_GOODS_USER 테이블에서 중고 거래 게시물을 3건 이상 등록한 사용자의 사용자 ID, 닉네임, 전체주소, 전화번호를 조회하는 SQL문을 작성해주세요. 이때, 전체 주소는 시, 도로명 주소, 상세 주소가 함께 출력되도록 해주시고, 전화번호의 경우 xxx-xxxx-xxxx 같은 형태로 하이픈 문자열(-)을 삽입하여 출력해주세요. 결과는 회원 ID를 기준으로 내림차순 정렬해주세요.

select writer_id,  NICKNAME, concat(CITY, " ", STREET_ADDRESS1, " ", STREET_ADDRESS2), concat(substr(TLNO, 1, 3), "-",substr(TLNO, 4, 4), "-", substr(TLNO, 8, 4))
from
(
SELECT writer_id, count(1) cnt,  NICKNAME, CITY, STREET_ADDRESS1, STREET_ADDRESS2, TLNO
from used_goods_board b left join used_goods_user u on b.writer_id = u.user_id
group by writer_id
) sub
where cnt >= 3
order by writer_id desc