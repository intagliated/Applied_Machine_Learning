import joblib
import numpy as np
def score(text: str, model, threshold: float):
    propensity = model.predict_proba([text])[0][1]
    prediction = bool(propensity >= threshold)
    return prediction, float(propensity)