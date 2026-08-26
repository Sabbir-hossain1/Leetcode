# Write your MySQL query statement below
SELECT 
e.name as name,
b.bonus as bonus

FROM employee as e
left join bonus as b
on e.empid = b.empid
where b.bonus<1000 or b.bonus is null