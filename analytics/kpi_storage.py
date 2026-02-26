import json
import os

KPI_FILE = "analytics/kpi_cache.json"


def save_kpi(data):
    with open(KPI_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_kpi():
    if not os.path.exists(KPI_FILE):
        return None

    with open(KPI_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
