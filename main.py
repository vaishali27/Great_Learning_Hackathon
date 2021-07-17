import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from ml_utils import load_model, predict, predict_v1
import datetime

app = FastAPI(
    title="Iris Predictor",
    docs_url="/"
)

app.add_event_handler("startup", load_model)

class QueryIn(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class QueryOut(BaseModel):
    flower_class: str


class QueryOutV1(BaseModel):
    flower_class: str
    timestamp: str


@app.get("/ping")
def ping():
    return {"ping": "pong"}


@app.post("/predict_flower", response_model=QueryOut, status_code=200)
def predict_flower(
    query_data: QueryIn
):
    output = {'flower_class': predict(query_data)}
    return output

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8888, reload=True)



@app.post("/predict_flower_v1", response_model=QueryOutV1, status_code=200)
def predict_flower(
    query_data: QueryIn
):
    output = {'flower_class': predict_v1(query_data), "timestamp": str(datetime.now())}
    return output

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8888, reload=True)