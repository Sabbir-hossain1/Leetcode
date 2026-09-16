-- Write your PostgreSQL query statement below
WITH consecutive as (
select 
	num,
	LAG(num,1) over(order by id) as prev_num,
	LAG(num,2) over(order by id) as prev_prev_num
from logs
)
select distinct num as ConsecutiveNums
from consecutive
where num = prev_num
	and num = prev_prev_num;