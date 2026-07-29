# Hate Speech Detection using Hinglish & Manglish NLP

## 📌 Project Overview

Hate Speech Detection is a Natural Language Processing (NLP) based machine learning project that identifies whether a given text contains hate speech or non-hate speech content.

The main objective of this project is to detect offensive and hateful content written in multilingual social media languages, especially **Hinglish (Hindi + English)** and **Manglish (Malayalam + English)** texts.

The system uses text preprocessing techniques, TF-IDF feature extraction, and a machine learning classification model to predict the category of user input.

---

## 🎯 Problem Statement

With the rapid growth of social media platforms, users frequently communicate using mixed languages. Traditional hate speech detection systems often fail to understand regional language combinations like Hinglish and Manglish.

This project aims to build an NLP-based model that can automatically detect harmful or hateful text written in mixed-language formats.

---

## 🚀 Features

- Detects hate speech from text input
- Supports Hinglish and Manglish language patterns
- Text preprocessing and cleaning
- TF-IDF based feature extraction
- Machine learning based classification
- Interactive Streamlit web application
- Real-time prediction

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Libraries & Frameworks
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Pickle

### Machine Learning Techniques
- Text preprocessing
- TF-IDF Vectorization
- Logistic Regression Classification

---

## 📂 Project Structure

```
Hate_Speech_Detection/
│
├── app.py                  # Streamlit application
├── preprocess.py           # Text preprocessing functions
├── model.pkl               # Trained ML model
├── vectorizer.pkl          # TF-IDF vectorizer
├── requirements.txt        # Required libraries
├── dataset/
│   └── final_hinglish_manglish_dataset.csv
│
└── README.md
```

---

## 📊 Dataset Details

The dataset contains multilingual social media text samples written in:

- English
- Hinglish
- Manglish

Each text sample is labelled as:

- **0 → Non-Hate Speech**
- **1 → Hate Speech**

The dataset is used for training and evaluating the machine learning model.

---

## ⚙️ Methodology

### 1. Data Collection
Collected Hinglish and Manglish text samples containing normal and hateful content.

### 2. Data Preprocessing
Performed:
- Lowercase conversion
- Removing unwanted characters
- Removing extra spaces
- Text normalization

### 3. Feature Extraction
Converted text into numerical features using:

**TF-IDF (Term Frequency-Inverse Document Frequency)**

### 4. Model Training
Trained a machine learning classifier using extracted features.

### 5. Prediction
The trained model predicts whether the given input text is:

- Hate Speech
- Non-Hate Speech

---

## 📈 Model Performance

The model was evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-score
- Classification Report

Model performance may vary depending on dataset quality and preprocessing techniques.

---

## 💻 Installation & Setup

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### Step 2: Navigate to project folder

```bash
cd Hate_Speech_Detection
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run Streamlit application

```bash
streamlit run app.py
```

---

## 🖥️ Application Usage

1. Open the Streamlit web application.
2. Enter any Hinglish, Manglish, or English text.
3. Click on the prediction button.
4. The system displays whether the text is classified as hate speech or not.

---

## 🔮 Future Enhancements

- Implement deep learning models like LSTM and Transformers
- Support more regional languages
- Improve accuracy with larger datasets
- Add multilingual sentiment analysis
- Deploy the application using cloud platforms

---

## 🌍 Applications

- Social media monitoring
- Online community moderation
- Cyberbullying detection
- Content filtering systems
- Digital safety platforms

---

## 👩‍💻 Developed By

**Shahista Afreen**

Hate Speech Detection using Hinglish & Manglish NLP
