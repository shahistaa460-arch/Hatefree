import joblib

model = joblib.load("models/hate_model.pkl")
vectorizer = joblib.load("models/hate_vectorizer.pkl")

while True:
    text = input("Enter text: ")

    X = vectorizer.transform([text])

    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0]

    print("Prediction:", pred)
    print("Probabilities:", prob)

    if pred == 1:
        print("🚨 Hate Speech")
    else:
        print("✅ Non-Hate")