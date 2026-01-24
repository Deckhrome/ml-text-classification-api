import joblib
import numpy as np

class NBASurvivalModel:
    def __init__(self, model_path: str, scaler_path: str, threshold_path: str):
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)

        with open(threshold_path, "r") as f:
            self.threshold = float(f.read())

    def predict(self, features: list):
        """
        features: list of numeric features in correct order
        """

        X = np.array(features).reshape(1, -1)
        X = np.nan_to_num(X, nan=0.0)
        X_scaled = self.scaler.transform(X)

        proba = self.model.predict_proba(X_scaled)[0, 1]
        prediction = int(proba >= self.threshold)

        decision = "Invest" if prediction == 1 else "Do not invest"

        return {
            "probability": float(proba),
            "prediction": prediction,
            "decision": decision
        }
