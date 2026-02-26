from analytics.kpi.monthly import calculate_monthly_stats
from analytics.kpi.profile import calculate_average_profile
from analytics.kpi.profitability import calculate_most_profitable_category
from analytics.kpi.total import calculate_total_tourists
from utils.safe_json import safe_float


def calculate_kpi():
    avg_age, avg_expenses, gender_mode = calculate_average_profile()

    total = calculate_total_tourists()
    monthly = calculate_monthly_stats()
    profitable = calculate_most_profitable_category()
    return {
        "total_tourists": total,

        "monthly_stats": [
            {"month": str(row[0]), "total": row[1]}
            for row in monthly
        ],
        "most_profitable_category": {
            "category": profitable[0] if profitable else None,
            "revenue": safe_float(profitable[1] if profitable else 0)
        },

        "average_profile": {
            "avg_age": safe_float(avg_age),
            "avg_expenses_mln": safe_float(avg_expenses),
            "most_common_gender": gender_mode[0] if gender_mode else None
        }
    }

