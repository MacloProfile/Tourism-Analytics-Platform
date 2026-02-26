from flask import Blueprint, request, jsonify
from sqlalchemy import text
from datetime import datetime

from analytics.sql.tourists import TOURISTS_BY_PERIOD
from app.db import db

tourists_router = Blueprint("tourists_router", __name__)


@tourists_router.route("/tourists", methods=["GET"])
def tourists_by_period():

    start = request.args.get("start")
    end = request.args.get("end")

    if not start or not end:
        return jsonify({"error": "Provide start and end dates"}), 400

    try:
        datetime.strptime(start, "%Y-%m-%d")
        datetime.strptime(end, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400

    total = db.session.execute(
        text(TOURISTS_BY_PERIOD),
        {"start_date": start, "end_date": end}
    ).scalar()

    return jsonify({
        "start": start,
        "end": end,
        "total_tourists": total
    })
