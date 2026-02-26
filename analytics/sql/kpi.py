MONTHLY_STATS = """
SELECT date_trunc('month', visit_date) AS month,
               COUNT(id) AS total
FROM tourism_data
GROUP BY date_trunc('month', visit_date)
ORDER BY month;
"""

AVG_EXPENSES = """
SELECT AVG(expenses_mln)
FROM tourism_data
WHERE expenses_mln IS NOT NULL
AND expenses_mln::text <> 'NaN';
"""

MOST_PROFITABLE_CATEGORY = """
SELECT tourist_category,
       COALESCE(SUM(expenses_mln), 0) AS revenue
FROM tourism_data
WHERE expenses_mln IS NOT NULL
AND expenses_mln::text <> 'NaN'
GROUP BY tourist_category
ORDER BY revenue DESC
LIMIT 1;
"""

TOTAL_TOURISTS = """
SELECT COUNT(id)
FROM tourism_data;
"""

AVG_AGE_PROFILE = """
SELECT AVG(age_group)
FROM tourism_data
WHERE age_group IS NOT NULL;
"""

AVG_EXPENSES_PROFILE = """
SELECT AVG(expenses_mln)
FROM tourism_data
WHERE expenses_mln IS NOT NULL
AND expenses_mln::text <> 'NaN';
"""

GENDER_MODE_PROFILE = """
SELECT gender, COUNT(id) AS cnt
FROM tourism_data
GROUP BY gender
ORDER BY cnt DESC
LIMIT 1;
"""