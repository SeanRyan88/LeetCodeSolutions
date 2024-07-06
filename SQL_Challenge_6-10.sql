--  Challenge 6
select eu.unique_id as unique_id, e.name as name
from Employees e left join EmployeeUNI eu on e.id = eu.id


--  Challenge 7
select b.product_name, a.year, a.price
from Sales as a
Join Product as b 
on a.product_id  = b.product_id;

--  Challenge 8
select v.customer_id, count(v.visit_id) as count_no_trans
from Visits v
left join Transactions t
on v.visit_id = t.visit_id
where t.transaction_id is null
group by v.customer_id;

--  Challenge 9
select w1.id
from Weather as w1
join Weather as w2
on w1.recordDate = Date_Add(w2.recordDate, interval 1 DAY)
where w1.temperature > w2.temperature;

-- Challenge 10
select a1.machine_id, round(avg(a2.timestamp - a1.timestamp), 3) as processing_time
from Activity a1
join Activity a2
on a1.machine_id = a2.machine_id 
and a1.process_id = a2.process_id
and a1.activity_type='start' and a2.activity_type='end'
group by a1.machine_id;