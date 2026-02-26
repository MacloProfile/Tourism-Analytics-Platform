from sqlalchemy import text

from analytics.sql.kpi import MONTHLY_STATS
from app.db import db


def calculate_monthly_stats():
    return db.session.execute(text(MONTHLY_STATS)).all()
