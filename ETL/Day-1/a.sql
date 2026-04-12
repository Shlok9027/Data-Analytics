CREATE database Companny;
use companny;
CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
    age INT
);

INSERT INTO employee(name, department, salary, age)
VALUES
('Rahul', 'IT', 60000, 26),
('Priya', 'HR', 45000, 28),
('Amit', 'Finance', 55000, 32),
('Neha', 'IT', 70000, 30),
('Karan', 'Marketing', 50000, 27),
('Anjali', 'IT', 65000, 29),
('Vikas', 'Finance', 52000, 31);


select * from employee;


with avg_salary as 
	(select  avg(salary) as avg_salary from employee)
    
select *
 from employee, avg_salary;

-- Find employees earning above average salary --
    
    
with avg_salary as 
	(select avg(salary) as avg_sal from employee)
    
select * from employee
where salary > (select avg_sal from avg_salary);



-- Find total salary per department

