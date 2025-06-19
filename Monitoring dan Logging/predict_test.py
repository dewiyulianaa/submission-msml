import requests
import json

# URL endpoint sesuai port mlflow serve
url = "http://127.0.0.1:5001/invocations"

# Header untuk format JSON split (format dataframe)
headers = {"Content-Type": "application/json"}

# Data input dalam format 'split' (urutan kolom harus sama dengan training)
data = {
    "dataframe_split": {
        "columns": [
            "BusinessTravel", "Department", "EducationField", "Gender", "JobRole",
            "MaritalStatus", "Over18", "OverTime", "Age", "DailyRate", "DistanceFromHome",
            "Education", "EmployeeNumber", "EnvironmentSatisfaction", "HourlyRate",
            "JobInvolvement", "JobLevel", "JobSatisfaction", "MonthlyIncome", "MonthlyRate",
            "NumCompaniesWorked", "PercentSalaryHike", "PerformanceRating",
            "RelationshipSatisfaction", "StandardHours", "StockOptionLevel",
            "TotalWorkingYears", "TrainingTimesLastYear", "WorkLifeBalance",
            "YearsAtCompany", "YearsInCurrentRole", "YearsSinceLastPromotion",
            "YearsWithCurrManager", "EmployeeCount"
        ],
        "data": [[
            "Travel_Rarely", "Research & Development", "Life Sciences", "Female", "Laboratory Technician",
            "Single", "Y", "Yes", 28, 800, 10,
            3, 1234, 3, 60,
            3, 1, 4, 5000, 21000,
            1, 12, 3,
            3, 80, 1,
            8, 3, 3,
            3, 3, 0,
            3, 1
        ]]
    }
}

# Kirim request POST ke endpoint model
response = requests.post(url, headers=headers, data=json.dumps(data))

# Tampilkan hasil prediksi
print("Prediction:", response.json())
