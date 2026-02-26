from app.db import db
from app.models.tourism import TourismData
from utils.average_age import parse_age_value


def load(df):
    objects = []

    for _, row in df.iterrows():
        obj = TourismData(
            visit_date=row["visit_date"],
            region_from=row["region_from"],
            age=row.get("age"),
            age_group=parse_age_value(row.get("age")),
            gender=row.get("gender"),
            tourist_category=row.get("tourist_category"),
            expenses_mln=row.get("expenses_mln"),
        )
        objects.append(obj)

    db.session.bulk_save_objects(objects)
    db.session.commit()