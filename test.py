import pytest
import joblib
from score import score
def test_score():
    model = joblib.load("model.joblib")
    pred, prop = score("test", model, 0.5)
    assert isinstance(pred, bool)