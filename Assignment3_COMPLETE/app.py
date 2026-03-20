from flask import Flask, request, jsonify
import joblib
from score import score
app = Flask(__name__)
model = joblib.load("model.joblib")
@app.route('/score', methods=['POST'])
def score_endpoint():
    data = request.get_json()
    p, pr = score(data.get('text', ''), model, data.get('threshold', 0.5))
    return jsonify({"prediction": p, "propensity": pr})
if __name__ == '__main__':
    app.run(port=5000)