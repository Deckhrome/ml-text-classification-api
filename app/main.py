from fastapi import FastAPI
from pydantic import BaseModel
# import model  # Assuming a model.py file exists with a predict function
from model import TextClassificationModel

class Item(BaseModel):
    text: str


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict")
def create_item(item: Item):
    input_text = item.text
    prediction = "positive" if "good" in input_text.lower() else "negative"

    # label, confidence = model.predict(input_text)

    return {"text": input_text, "predicted_label": prediction}
