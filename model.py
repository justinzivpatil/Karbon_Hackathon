# model.py
from rules import latest_financial_index, total_revenue_5cr_flag, iscr_flag, borrowing_to_revenue_flag
import json

def probe_model_5l_profit(data: dict):
    lastest_financial_index_value = latest_financial_index(data)
    total_revenue_5cr_flag_value = total_revenue_5cr_flag(data, lastest_financial_index_value)
    borrowing_to_revenue_flag_value = borrowing_to_revenue_flag(data, lastest_financial_index_value)
    iscr_flag_value = iscr_flag(data, lastest_financial_index_value)

    return {
        "flags": {
            "TOTAL_REVENUE_5CR_FLAG": total_revenue_5cr_flag_value,
            "BORROWING_TO_REVENUE_FLAG": borrowing_to_revenue_flag_value,
            "ISCR_FLAG": iscr_flag_value,
        }
    }

if __name__ == "__main__":
    with open("data.json", "r") as file:
        content = file.read()
        data = json.loads(content)
        result = probe_model_5l_profit(data["data"])
        print(json.dumps(result, indent=4))
