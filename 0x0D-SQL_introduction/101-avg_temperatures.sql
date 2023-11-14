-- avrege by city order by temp
SELECT city, AGV(value) as 'avg_tmp'
FROM temperatures
GROUP BY city
ORDER BY avg_tmp DESC