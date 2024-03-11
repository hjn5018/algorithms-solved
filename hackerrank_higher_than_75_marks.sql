-- select Name from STUDENTS where Marks > 75
-- order by Name 


-- select regexp_substr(Name, '\\w{3}$') from STUDENTS
-- tha
-- lia
-- ney

-- select Name from STUDENTS
-- Samantha
-- Julia
-- Britney


-- select regexp_substr(Name, '\\w{3}$') from STUDENTS where Marks > 75

-- select regexp_substr(Name, '\\w{3}$') from STUDENTS where Marks > 75 order by 1, ID

select Name from STUDENTS where Marks > 75 order by regexp_substr(Name, '\\w{3}$'), ID
