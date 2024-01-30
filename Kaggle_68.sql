-- 2022년 1월의 도서 판매 데이터를 기준으로 저자 별, 카테고리 별 매출액(TOTAL_SALES = 판매량 * 판매가) 을 구하여, 저자 ID(AUTHOR_ID), 저자명(AUTHOR_NAME), 카테고리(CATEGORY), 매출액(SALES) 리스트를 출력하는 SQL문을 작성해주세요. 결과는 저자 ID를 오름차순으로, 저자 ID가 같다면 카테고리를 내림차순 정렬해주세요.

select sub1.author_id, author_name, category, total_sales
from
(
select author_id, category, sum(sales * price) total_sales
from book_sales s left join book b on s.book_id = b.book_id
where date_format(date(sales_date), '%m') = 01
group by author_id, category
) sub1 left join author a on sub1.author_id = a.author_id
order by 1, 3 desc


-- subquery를 두 번 사용할 때, Duplicate column name 에러가 간혹 발생한다.
-- 첫 번째로 적용한 subquery에서 이름이 중복인 컬럼을 뜻하므로 한 쪽 테이블의 컬럼명을 바꾸면 실행된다.