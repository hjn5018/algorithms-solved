select w.id, p.age, w.coins_needed, w.power
from wands_property p
left join wands w
on p.code = w.code
where is_evil = 0
-- age별, power별 coins_needed rank를 재고 1을 추출해서 반환하면 될 것 같은데...
