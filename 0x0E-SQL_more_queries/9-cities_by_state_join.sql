-- Task 9. Cities by States
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.states_id = states.id
