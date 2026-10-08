-- approach 1
select class
from courses
group by class
having count(student)>=5

--approach 2

-- select class
-- from 
-- (select class, count(student) as student_count
-- from courses
-- group by class
-- ) t
-- where student_count>=5