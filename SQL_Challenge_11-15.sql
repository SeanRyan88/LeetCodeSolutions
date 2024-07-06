-- Challenge 11 - 557. Employee Bonus
select e.name, b.bonus
from Employee e
left join Bonus b
on e.empId = b.empId
where b.bonus < 1000 or b.bonus is null;

-- Challenge 12 - 1280. Students and Examinations
select s.student_id, s.student_name, su.subject_name, count(e.student_id) as attended_exams
from Students s
cross join Subjects su
left join Examinations e
on s.student_id = e.student_id and su.subject_name = e.subject_name
group by s.student_id, s.student_name, su.subject_name
order by s.student_id, su.subject_name

-- Challenge 13 - 570. Managers with at Least 5 Direct Reports
select e1.name
from Employee e1
join Employee e2 on e1.id = e2.managerId
group by e1.id
having count(*) >= 5

select e1.name
from Employee e1
join (
    select managerId, count(*) as Reports
    from Employee
    group by managerId
    having Count(*) >= 5
) E2 on e1.id = e2.managerId

-- Challenge 14 - 1934. Confirmation Rate
select s.user_id, ifnull(round(sum(action = 'confirmed') / count(*), 2), 0.00) as confirmation_rate
from Signups s
left join Confirmations c on s.user_id = c.user_id
group by s.user_id