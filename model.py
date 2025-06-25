import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Sample music reviews
data = {
    "review": [
        "This song is an absolute masterpiece!",
        "Worst track I’ve ever heard in my life.",
        "Loved the energy and vibe of the music.",
        "Painfully boring. I couldn’t finish it.",
        "The beats and vocals were amazing!",
        "It sounded like noise. No melody, no soul."
    ],
    "label": [1, 0, 1, 0, 1, 0]  # 1 = Positive, 0 = Negative
}

df = pd.DataFrame(data)

# Vectorize the reviews
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["review"])
y = df["label"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save the model and vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("✅ Music review sentiment model and vectorizer saved.")
