from flask import Blueprint, jsonify

from analytics.get_kpi import calculate_kpi
from analytics.kpi_storage import load_kpi, save_kpi

kpi_router = Blueprint("kpi_router", __name__)


@kpi_router.route("/kpi", methods=["GET"])
def get_kpi():
    data = load_kpi()

    if data is None:
        data = calculate_kpi()
        save_kpi(data)

    return jsonify(data), 200


@kpi_router.route("/kpi/recalculate", methods=["POST"])
def recalc_kpi():
    data = calculate_kpi()
    save_kpi(data)

    return jsonify({
        "status": "success",
        "message": "kpi recalculated",
        "data": data
    }), 200
