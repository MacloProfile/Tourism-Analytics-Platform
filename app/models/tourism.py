from app.db import db


class TourismData(db.Model):
    __tablename__ = "tourism_data"

    id = db.Column(db.Integer, primary_key=True)
    visit_date = db.Column(db.Date, nullable=False)
    region_from = db.Column(db.String(255), nullable=False)
    age = db.Column(db.String(100))
    age_group = db.Column(db.Integer)
    gender = db.Column(db.String(50))
    tourist_category = db.Column(db.String(100))
    expenses_mln = db.Column(db.Numeric)
