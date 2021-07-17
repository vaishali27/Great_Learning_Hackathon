import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from ml_utils import CreditScoreModel

app = FastAPI(
    title="Credit Risk",
    docs_url="/"
)


class QueryIn(BaseModel):
    Status_of_existing_checking_account: str
    Credit_history: str
    Purpose: str
    Savings_account_bonds: str
    Present_employment_since: str
    Personal_status_and_sex:str
    Other_debtors_guarantors:str
    Property:str
    Other_installment_plans:str
    Housing:str
    Job: str
    Telephone: str
    foreign_worker: str
    Duration_in_month: int
    Credit_amount: int
    Installment_rate_in_percentage_of_disposable_income: int
    Present_residence_since: int
    Age_in_years: int
    Number_of_existing_credits_at_this_bank: int
    Number_of_people_being_liable_to_provide_maintenance_for: int

class QueryOut(BaseModel):
    credit_risk: str



@app.get("/ping")
def ping():
    return {"ping": "pong"}


@app.post("/predict_credit_risk", response_model=QueryOut, status_code=200)
def predict_credit_risk(query_data: QueryIn):
    model = CreditScoreModel()
    output = {'credit_risk': model.predict(query_data)}
    return output

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8888, reload=True)

