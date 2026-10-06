
--approach 1
select customer_number
from Orders
group by customer_number
order by count(*) desc
limit 1

-- approach 2
-- select customer_number
-- from orders
-- group by customer_number
-- having count(*) = (select max(order_number)
-- from (
--     select count(*) order_number
--     from orders 
--     group  by customer_number
-- ) as counts
-- )

-- approach 3
-- select customer_number
-- from 
-- (select 
-- customer_number,
-- count(*) as order_count,
-- rank() over(order by count(*) desc) as rnk
-- from orders
-- group by customer_number
-- ) as t
-- where rnk=1;

-- approach 4
-- select customer_number
-- from (
-- select customer_number,
-- dense_rank() over(order by count(*) desc) as rnk
-- from orders
-- group by customer_number
-- ) as t
-- where rnk=1