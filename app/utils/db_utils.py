import time
from sqlalchemy import text
from app.db import db


def wait_for_database(app, retries=10, delay=2):
    with app.app_context():
        for _ in range(retries):
            try:
                db.session.execute(text("SELECT 1"))
                db.create_all()
                return
            except Exception:
                time.sleep(delay)

        raise Exception("Database connection failed")
