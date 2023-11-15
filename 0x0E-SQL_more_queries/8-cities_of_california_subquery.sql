-- select
SELECT id, state_id, name
FROM cities
WHERE state_id IN(
    SELECT id from states
    WHERE name = 'alifornia'
)
ORDER BY id;