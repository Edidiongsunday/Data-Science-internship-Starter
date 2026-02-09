-- Week 4: SQL Queries - Practice Exercises
-- Your task: Complete the SQL exercises below
-- Instructions: Uncomment and complete each query. Add your own queries at the end!

-- ============================================
-- DATABASE SETUP (CREATE SAMPLE DATA)
-- ============================================

-- Create Employees table
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary INT,
    years_experience INT,
    hire_date DATE
);

-- Create Sales table
CREATE TABLE IF NOT EXISTS sales (
    sale_id INT PRIMARY KEY,
    employee_id INT,
    sale_amount DECIMAL(10, 2),
    sale_date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- Create Departments table
CREATE TABLE IF NOT EXISTS departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50),
    budget INT
);

-- Insert sample data
INSERT INTO employees VALUES
(1, 'Alice Johnson', 'Sales', 60000, 5, '2019-01-15'),
(2, 'Bob Smith', 'IT', 75000, 7, '2017-03-22'),
(3, 'Charlie Brown', 'HR', 55000, 3, '2021-06-10'),
(4, 'Diana Prince', 'Sales', 65000, 6, '2018-09-05'),
(5, 'Eve Wilson', 'IT', 80000, 10, '2012-11-20');

INSERT INTO sales VALUES
(101, 1, 5000, '2024-01-05'),
(102, 1, 7500, '2024-01-10'),
(103, 2, 3000, '2024-01-08'),
(104, 4, 6000, '2024-01-12'),
(105, 4, 8000, '2024-01-15'),
(106, 1, 4500, '2024-01-18');

INSERT INTO departments VALUES
(1, 'Sales', 500000),
(2, 'IT', 800000),
(3, 'HR', 300000);

-- ============================================
-- BASIC QUERIES
-- ============================================

-- EXERCISE 1: Select all employees
-- TODO: Write a query to select all employee records
-- SELECT * FROM employees;

-- EXERCISE 2: Select employee names and salaries
-- TODO: Write a query to show only names and salaries
-- SELECT name, salary FROM employees;

-- EXERCISE 3: Filter employees by department
-- TODO: Write a query to find all IT department employees
-- SELECT * FROM employees WHERE department = 'IT';

-- EXERCISE 4: Filter by salary threshold
-- TODO: Write a query to find employees earning more than $60,000
-- SELECT name, salary FROM employees WHERE salary > 60000;

-- ============================================
-- SORTING & LIMITING
-- ============================================

-- EXERCISE 5: Top earners
-- TODO: Write a query to find the highest paid employee
-- SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 1;

-- EXERCISE 6: Recent hires
-- TODO: Write a query to find the 3 most recently hired employees
-- SELECT name, hire_date FROM employees ORDER BY hire_date DESC LIMIT 3;

-- ============================================
-- AGGREGATE FUNCTIONS
-- ============================================

-- EXERCISE 7: Count total employees
-- TODO: Write a query to count total number of employees
-- SELECT COUNT(*) as total_employees FROM employees;

-- EXERCISE 8: Average salary by department
-- TODO: Write a query to find the average salary for each department
-- SELECT department, AVG(salary) as avg_salary 
-- FROM employees 
-- GROUP BY department;

-- EXERCISE 9: Total sales amount
-- TODO: Write a query to find the total sales amount
-- SELECT SUM(sale_amount) as total_sales FROM sales;

-- EXERCISE 10: Sales per employee
-- TODO: Write a query to show total sales for each employee
-- SELECT e.name, COUNT(s.sale_id) as sales_count, SUM(s.sale_amount) as total_sales
-- FROM employees e
-- LEFT JOIN sales s ON e.employee_id = s.employee_id
-- GROUP BY e.employee_id, e.name;

-- ============================================
-- JOIN OPERATIONS
-- ============================================

-- EXERCISE 11: Employee and their sales (INNER JOIN)
-- TODO: Write a query to show employees and their sales
-- SELECT e.name, s.sale_amount, s.sale_date
-- FROM employees e
-- INNER JOIN sales s ON e.employee_id = s.employee_id;

-- EXERCISE 12: All employees with their sales (LEFT JOIN)
-- TODO: Write a query to show all employees even if they have no sales
-- SELECT e.name, COUNT(s.sale_id) as number_of_sales
-- FROM employees e
-- LEFT JOIN sales s ON e.employee_id = s.employee_id
-- GROUP BY e.employee_id, e.name;

-- ============================================
-- FILTERING GROUPS (HAVING)
-- ============================================

-- EXERCISE 13: Departments with 2+ employees
-- TODO: Write a query to find departments with more than 1 employee
-- SELECT department, COUNT(*) as employee_count
-- FROM employees
-- GROUP BY department
-- HAVING COUNT(*) > 1;

-- EXERCISE 14: High performers
-- TODO: Write a query to find employees who made more than 3 sales
-- SELECT e.name, COUNT(s.sale_id) as sale_count
-- FROM employees e
-- JOIN sales s ON e.employee_id = s.employee_id
-- GROUP BY e.employee_id, e.name
-- HAVING COUNT(s.sale_id) > 1;

-- ============================================
-- ADVANCED QUERIES
-- ============================================

-- EXERCISE 15: Employee salary rank
-- TODO: Write a query to rank employees by salary
-- SELECT name, salary, 
--        RANK() OVER (ORDER BY salary DESC) as salary_rank
-- FROM employees;

-- EXERCISE 16: Sales statistics
-- TODO: Write a query to find min, max, avg sales amount
-- SELECT 
--    MIN(sale_amount) as min_sale,
--    MAX(sale_amount) as max_sale,
--    AVG(sale_amount) as avg_sale,
--    COUNT(*) as total_sales
-- FROM sales;

-- ============================================
-- YOUR CUSTOM QUERIES (Write 3 new ones!)
-- ============================================

-- EXERCISE 17: TODO - Write your own query question and answer
-- Question: 
-- Answer:

-- EXERCISE 18: TODO - Write your own query question and answer
-- Question: 
-- Answer:

-- EXERCISE 19: TODO - Write your own query question and answer
-- Question: 
-- Answer:

-- ============================================
-- NOTES
-- ============================================

/*
COMMON SQL PATTERNS:

1. Basic Select with Filter
   SELECT columns FROM table WHERE condition;

2. Aggregates
   SELECT department, COUNT(*), AVG(salary)
   FROM employees
   GROUP BY department;

3. Join
   SELECT e.name, s.sale_amount
   FROM employees e
   JOIN sales s ON e.employee_id = s.employee_id;

4. Subquery
   SELECT * FROM employees
   WHERE salary > (SELECT AVG(salary) FROM employees);

5. Case Statement
   SELECT name,
          CASE WHEN salary > 70000 THEN 'High'
               WHEN salary > 55000 THEN 'Medium'
               ELSE 'Low' END as salary_level
   FROM employees;

REMEMBER:
- SQL keywords are case-insensitive but best practice is UPPERCASE
- Always use aliases for clarity (AS)
- Test queries on small datasets first
- Use meaningful column names in results
*/
