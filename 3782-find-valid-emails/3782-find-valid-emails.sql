# Write your MySQL query statement below
select * from Users
where REGEXP_LIKE(email, '[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.com$')