# Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

select w1.id
from weather w1, weather w2
where datediff(w1.recordDate, w2.recordDate) = 1 and w1.temperature > w2.temperature

