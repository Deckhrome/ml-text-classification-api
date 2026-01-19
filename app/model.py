import json
import joblib
from typing import Dict, Any

class TextClassificationModel:
    def __init__(self, model_path: str):
        # Load the pre-trained model
        self.model = joblib.load(model_path)

    def predict(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        # Extract the text from the input JSON
        text = input_data.get("text", "")
        if not text:
            return {"error": "No text provided for prediction"}

        # Perform prediction
        prediction = self.model.predict([text])
        predicted_label = prediction[0]

        # Return the prediction in JSON format
        return {"text": text, "predicted_label": predicted_label}