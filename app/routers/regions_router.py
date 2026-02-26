from flask import Blueprint, jsonify
from sqlalchemy import text

from analytics.sql.regions import REGIONS_DISTRIBUTION
from app.db import db

regions_router = Blueprint("regions_router", __name__)


@regions_router.route("/regions", methods=["GET"])
def regions():
    results = db.session.execute(text(REGIONS_DISTRIBUTION)).all()

    return jsonify([
        {"region": row[0], "total": row[1]}
        for row in results
    ])
