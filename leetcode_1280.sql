# Write a solution to find the number of times each student attended each exam.
# Return the result table ordered by student_id and subject_name.

select st.student_id, st.student_name, su.subject_name, count(ex.student_id) attended_exams
from Students st
cross join Subjects su
left join Examinations ex on st.student_id = ex.student_id and su.subject_name = ex.subject_name
group by st.student_id, su.subject_name
order by st.student_id, su.subject_name