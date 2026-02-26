from sqlalchemy import text

from analytics.sql.kpi import TOTAL_TOURISTS
from app.db import db


def calculate_total_tourists():
    return db.session.execute(text(TOTAL_TOURISTS)).scalar()
