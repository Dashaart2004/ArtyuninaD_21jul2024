1.SELECT DISTINCT  name
FROM Regions;

2.SELECT M.name,
m.season,
m.edible
from Mushrooms AS m
join Categories AS n
on m.category_id=n.category_id
where c.name= ‘Трубчатые’;

3.SELECT c.name,
COUNT(m.mushroom_id)
FROM Categories AS c
JOIN Mushrooms AS m
ON c.category_id=m.category_id
GROUP BY 
    c.category_id, c.name
ORDER BY 
    mushroom_count DESC;

4.SELECT m.name,
m.description
FROM Mushrooms AS m
JOIN Regions AS r
ON m.primary_region_id=r.primary_region_id
WHERE m.edible = TRUE 
AND r.id IN (
    SELECT id
    FROM regions
    ORDER BY size DESC
    LIMIT 5
)
ORDER BY r.size DESC, m.name;

5.SELECT m.name
FROM Mushrooms AS m
JOIN Categories AS c
ON m.category_id=c.category_id
JOIN Regions AS r
ON m.primary_region_id=r.primary_region_id
WHERE m.season= “Spring” AND 
c.name=”Пластинчатые” AND 
r.size <= 6000
