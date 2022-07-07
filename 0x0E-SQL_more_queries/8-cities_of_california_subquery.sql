-- Task 8. Cities of California y aguanten los ré jó
SELECT id, name FROM cities WHERE state_id = (
SELECT id
FROM states
WHERE name = "California")
