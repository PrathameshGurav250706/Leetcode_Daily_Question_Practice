# Write your MySQL query statement below
select m.name 
from Employee as m
join Employee as e
on m.id=e.managerId
group by m.id , m.name
having count(e.id)>=5;