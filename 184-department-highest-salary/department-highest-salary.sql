-- Write your PostgreSQL query statement below
-- with ranked_employees as (
--     select
--     e.name as Employee,
--     e.salary,
--     e.departmentid,
--     rank() over(partition by departmentid order by e.salary desc) salary_rank
--     from employee as e
-- )
-- select
-- d.name as Department,
-- e.employee as Employee,
-- e.salary as Salary
-- from ranked_employees as e
-- join department as d
-- on e.departmentid=d.id
-- where e.salary_rank=1

select 
d.name as Department,
e.name as Employee,
e.salary as Salary
from employee e
join department d
on e.departmentid=d.id
where (e.departmentid,e.salary)  in (
    select
    departmentid,
    max(salary)
    from employee
    group by departmentid
)

