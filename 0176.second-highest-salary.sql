--
-- @lc app=leetcode id=176 lang=mysql
--
-- [176] Second Highest Salary
--

-- @lc code=start
select max(salary) as SecondHighestSalary from Employee where salary < (select max(salary) from employee);
-- @lc code=end

