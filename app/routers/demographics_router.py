from flask import Blueprint, jsonify, request
from sqlalchemy import text

from analytics.sql.demographics import DEMOGRAPHICS_AVG_AGE, DEMOGRAPHICS_GENDER
from app.db import db

demographics_router = Blueprint("demographics_router", __name__)


@demographics_router.route("/demographics", methods=["GET"])
def demographics():
    avg_age = db.session.execute(text(DEMOGRAPHICS_AVG_AGE)).scalar()
    gender_distribution = db.session.execute(text(DEMOGRAPHICS_GENDER)).all()

    return jsonify({
        "average_age": avg_age,
        "gender_distribution": [
            {"gender": row[0], "total": row[1]}
            for row in gender_distribution
        ]
    })
