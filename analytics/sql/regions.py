REGIONS_DISTRIBUTION = """
SELECT region_from, COUNT(id) AS total
FROM tourism_data
GROUP BY region_from
ORDER BY total DESC;
"""
