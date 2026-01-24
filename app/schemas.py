from pydantic import BaseModel

class PlayerStatsRequest(BaseModel):
    GP: int
    MIN: float
    PTS: float
    FGM: float
    FGA: float
    FG_pct: float
    FG3M: float
    FG3A: float
    FG3_pct: float
    FTM: float
    FTA: float
    FT_pct: float
    OREB: float
    DREB: float
    REB: float
    AST: float
    STL: float
    BLK: float
    TOV: float


class PredictionResponse(BaseModel):
    probability: float
    prediction: int
    decision: str
