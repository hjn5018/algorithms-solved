select company.company_code,
       company.founder,
       count(employee.lead_manager_code),
       count(employee.senior_manager_code),
       count(employee.manager_code),
       count(employee.employee_code)
from company
join employee
on company.company_code = employee.company_code

-- 그냥 생각나는 대로 갈겨본 쿼리이다.
-- 이상하게 이 문제만 출력이 늦다.

-- 일단 해보기는 했지만, 하나씩 확인해가며 쿼리를 다듬어야겠다고 생각했다.
