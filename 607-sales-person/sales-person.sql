# Write your MySQL query statement below
-- Approach 1
select name
from salesperson
where sales_id not in
(select o.sales_id
from orders o
join company c
on c.com_id = o.com_id
where c.name = "RED")

# approach 2
-- select s.name
-- from salesperson s
-- left join
-- (select distinct o.sales_id
-- from Orders o
-- join company c
-- on o.com_id = c.com_id
-- where c.name="RED") red_sales
-- on s.sales_id = red_sales.sales_id
-- where red_sales.sales_id is null

#approach 3
-- select s.name
-- from salesperson s
-- where not exists
-- (select 1
-- from orders o
-- join company c
-- on c.com_id = o.com_id
-- where o.sales_id = s.sales_id
-- and c.name = "RED")
