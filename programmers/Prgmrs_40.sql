-- 동물 보호소에 들어온 동물 중 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물의 아이디와 이름, 성별 및 중성화 여부를 조회하는 SQL 문을 작성해주세요. 이때 결과는 아이디 순으로 조회해주세요. 

SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM animal_ins
where name IN('ELLA', 'LUCY', 'PICKLE', 'Rogan', 'Sabrina', 'Mitty')
order by 1