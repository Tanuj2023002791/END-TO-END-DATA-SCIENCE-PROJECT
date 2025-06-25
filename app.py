from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    review = data.get("review", "")
    features = vectorizer.transform([review])
    prediction = model.predict(features)[0]
    confidence = model.predict_proba(features)[0][prediction]
    sentiment = "Positive" if prediction == 1 else "Negative"
    return jsonify({
        "sentiment": sentiment,
        "confidence": round(float(confidence), 4)
    })

@app.route("/")
def home():
    return "🎧 Music Review Sentiment API is live!"

if __name__ == "__main__":
    app.run(debug=True)

