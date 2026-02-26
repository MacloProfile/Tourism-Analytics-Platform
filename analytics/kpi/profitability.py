from sqlalchemy import text

from analytics.sql.kpi import MOST_PROFITABLE_CATEGORY
from app.db import db


def calculate_most_profitable_category():
    return db.session.execute(text(MOST_PROFITABLE_CATEGORY)).first()
