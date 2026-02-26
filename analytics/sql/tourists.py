TOURISTS_BY_PERIOD = """
SELECT COUNT(id)
FROM tourism_data
WHERE visit_date >= :start_date
AND visit_date <= :end_date;
"""
