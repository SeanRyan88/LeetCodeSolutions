--  Challenge 5
select b.product_name, a.year, a.price
from Sales as a
Join Product as b 
on a.product_id  = b.product_id;

--  Challenge 6
select v.customer_id, count(v.visit_id) as count_no_trans
from Visits v
left join Transactions t
on v.visit_id = t.visit_id
where t.transaction_id is null
group by v.customer_id;

--  Challenge 7
select w1.id
from Weather as w1
join Weather as w2
on w1.recordDate = Date_Add(w2.recordDate, interval 1 DAY)
where w1.temperature > w2.temperature;

-- Challenge 8
select a1.machine_id, round(avg(a2.timestamp - a1.timestamp), 3) as processing_time
from Activity a1
join Activity a2
on a1.machine_id = a2.machine_id 
and a1.process_id = a2.process_id
and a1.activity_type='start' and a2.activity_type='end'
group by a1.machine_id;

-- Challenge 9
select e.name, b.bonus
from Employee e
left join Bonus b
on e.empId = b.empId
where b.bonus < 1000 or b.bonus is null;

-- Challenge 10
select s.student_id, s.student_name, su.subject_name, count(e.student_id) as attended_exams
from Students s
cross join Subjects su
left join Examinations e
on s.student_id = e.student_id and su.subject_name = e.subject_name
group by s.student_id, s.student_name, su.subject_name
order by s.student_id, su.subject_name