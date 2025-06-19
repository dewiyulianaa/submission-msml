import requests
import pandas as pd

data = pd.DataFrame([{
    "BusinessTravel_Travel_Frequently": 1,
    "BusinessTravel_Travel_Rarely": 0,
    "DailyRate": 1000,
    "Department_Research & Development": 1,
    "Department_Sales": 0,
    "Age": 35,
    "DistanceFromHome": 5,
    "MonthlyIncome": 6000,
    "TotalWorkingYears": 10,
    "YearsAtCompany": 5
    # ... sesuaikan dengan semua fitur hasil one-hot encoding
}])

input_json = {
    "dataframe_split": data.to_dict(orient="split")
}

response = requests.post(
    url="http://127.0.0.1:5001/invocations",
    headers={"Content-Type": "application/json"},
    json=input_json
)

print("Response:", response.json())
