import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("models/hate_model.pkl")
vectorizer = joblib.load("models/hate_vectorizer.pkl")

# Page configuration
st.set_page_config(
    page_title="HateFree",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ HateFree")
st.subheader("Code-Switched Hate Speech Detector")
st.write("Detects hate speech in Hinglish and Manglish text.")

# User input
text = st.text_area("Enter your text", height=150)

if st.button("Detect Hate Speech"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        text_vector = vectorizer.transform([text])

        prediction = model.predict(text_vector)[0]
        confidence = model.predict_proba(text_vector).max() * 100

        if prediction == 1:
            st.error("🚨 Hate Speech Detected")
        else:
            st.success("✅ Non-Hate Speech")

        st.info(f"Confidence: {confidence:.2f}%")