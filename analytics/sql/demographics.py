DEMOGRAPHICS_AVG_AGE = """
SELECT AVG(age_group)
FROM tourism_data
WHERE age_group IS NOT NULL;
"""

DEMOGRAPHICS_GENDER = """
SELECT gender, COUNT(id)
FROM tourism_data
GROUP BY gender
ORDER BY COUNT(id) DESC;
"""
