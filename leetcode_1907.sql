-- Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:
-- "Low Salary": All the salaries strictly less than $20000.
-- "Average Salary": All the salaries in the inclusive range [$20000, $50000].
-- "High Salary": All the salaries strictly greater than $50000.
-- The result table must contain all three categories. If there are no accounts in a category, return 0.

SELECT
    'Low Salary' as category,
    SUM(income < 20000) as accounts_count
FROM
    Accounts

UNION

SELECT
    'Average Salary' as category,
    SUM(income between 20000 and 50000) as accounts_count
FROM
    Accounts

UNION

SELECT
    'High Salary' as category,
    SUM(income > 50000) as accounts_count
FROM
    Accounts
