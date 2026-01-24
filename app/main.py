from fastapi import FastAPI
from app.model import NBASurvivalModel
from app.schemas import PlayerStatsRequest, PredictionResponse

app = FastAPI(
    title="NBA Player Investment API",
    description="Predict if a rookie will last more than 5 years in NBA",
    version="1.0"
)

model = None

@app.get("/")
def root():
    return {"message": "NBA Investment Prediction API"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.on_event("startup")
def load_model():
    global model
    model = NBASurvivalModel(
        model_path="app/models/svc_model.joblib",
        scaler_path="app/models/scaler.joblib",
        threshold_path="app/models/threshold.txt"
    )

@app.post("/predict", response_model=PredictionResponse)
def predict_player(request: PlayerStatsRequest):

    features = [
        request.GP,
        request.MIN,
        request.PTS,
        request.FGM,
        request.FGA,
        request.FG_pct,
        request.FG3M,
        request.FG3A,
        request.FG3_pct,
        request.FTM,
        request.FTA,
        request.FT_pct,
        request.OREB,
        request.DREB,
        request.REB,
        request.AST,
        request.STL,
        request.BLK,
        request.TOV,
    ]

    result = model.predict(features)
    return result
