from sqlalchemy import text

from analytics.sql.kpi import AVG_AGE_PROFILE, AVG_EXPENSES_PROFILE, GENDER_MODE_PROFILE
from app.db import db


def calculate_average_profile():
    avg_age = db.session.execute(text(AVG_AGE_PROFILE)).scalar()
    avg_expenses = db.session.execute(text(AVG_EXPENSES_PROFILE)).scalar()
    gender_mode = db.session.execute(text(GENDER_MODE_PROFILE)).first()

    return avg_age, avg_expenses, gender_mode
