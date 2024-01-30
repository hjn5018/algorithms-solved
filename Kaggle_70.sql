-- MEMBER_PROFILE와 REST_REVIEW 테이블에서 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회하는 SQL문을 작성해주세요. 회원 이름, 리뷰 텍스트, 리뷰 작성일이 출력되도록 작성해주시고, 결과는 리뷰 작성일을 기준으로 오름차순, 리뷰 작성일이 같다면 리뷰 텍스트를 기준으로 오름차순 정렬해주세요.

select member_name, b.review_text, date_format(b.review_date, '%Y-%m-%d') review_date
from member_profile m inner join
(
select *
from rest_review r inner join
(
SELECT member_id m_id, count(1) cnt
from rest_review
group by member_id
order by cnt desc
limit 1
) a on r.member_id = a.m_id
) b on m.member_id = b.member_id
order by 3, 2