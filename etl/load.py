from app.db import db
from app.models.tourism import TourismData
from utils.average_age import parse_age_value


def load(df, batch_size=5000):

    objects = []
    for i, row in enumerate(df.itertuples(index=False), 1):
        obj = TourismData(
            visit_date=row.visit_date,
            region_from=row.region_from,
            age=row.age,
            age_group=parse_age_value(row.age),
            gender=row.gender,
            tourist_category=row.tourist_category,
            expenses_mln=row.expenses_mln,
        )
        objects.append(obj)

        if i % batch_size == 0:
            db.session.bulk_save_objects(objects)
            db.session.commit()
            objects.clear()

    if objects:
        db.session.bulk_save_objects(objects)
        db.session.commit()
