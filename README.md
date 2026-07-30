# 🛡️ HateFree: Code-Switched Hate Speech Detection using Hinglish & Manglish

## 📌 Overview

HateFree is a Machine Learning-based web application that detects hate speech in **code-switched languages**, specifically **Hinglish (Hindi-English)** and **Manglish (Malayalam-English)**.

The project addresses the challenge of identifying offensive and hateful content in multilingual social media conversations, where users frequently mix English with regional Indian languages.

The application is built using **TF-IDF Vectorization**, **Logistic Regression**, and deployed with **Streamlit** for real-time prediction.

---

## 🎯 Problem Statement

Most hate speech detection systems are designed for English text and perform poorly on code-switched languages such as Hinglish and Manglish.

This project aims to develop a lightweight machine learning solution capable of classifying mixed-language text into:

- Hate Speech
- Non-Hate Speech

---

## ✨ Features

- Detects hate speech in Hinglish and Manglish text
- Machine Learning-based prediction
- Interactive Streamlit web application
- TF-IDF text feature extraction
- Logistic Regression classifier
- Model evaluation using multiple performance metrics
- Simple and lightweight deployment

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- Streamlit
- Joblib
- Jupyter Notebook

---

## 📂 Project Structure

```
Hate_Free/
│
├── data/
│   ├── hinglish/
│   │   ├── train.txt
│   │   └── test.txt
│   ├── manglish.xlsx
│   └── final_dataset.csv
│
├── models/
│   ├── hate_model.pkl
│   └── hate_vectorizer.pkl
│
├── screenshots/
│
├── app.py
├── preprocess.py
├── train.py
├── predict.py
├── evaluation.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset

The project combines two publicly available datasets:

### Hinglish Dataset
- Mixed Hindi-English text
- Labels mapped to binary classes

### Manglish Dataset
- Mixed Malayalam-English text
- Binary hate speech labels

Both datasets were:

- Cleaned
- Standardized
- Label mapped
- Merged
- Duplicate entries removed

Final Dataset Size:

**15,852 Samples**

---

## ⚙️ Workflow

```
Dataset Collection
        │
        ▼
Data Cleaning & Preprocessing
        │
        ▼
Merge Hinglish + Manglish Dataset
        │
        ▼
TF-IDF Feature Extraction
        │
        ▼
Logistic Regression Training
        │
        ▼
Model Evaluation
        │
        ▼
Model Saving
        │
        ▼
Prediction
        │
        ▼
Streamlit Web Application
```

---

## 🚀 Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project folder

```bash
cd Hate_Free
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Preprocess Dataset

```bash
python preprocess.py
```

### Train Model

```bash
python train.py
```

### Test Prediction

```bash
python predict.py
```

### Launch Streamlit App

```bash
streamlit run app.py
```

---

## 📈 Model Evaluation

The trained model was evaluated using a held-out test dataset.

Evaluation includes:

- Accuracy
- Precision
- Recall
- F1-Score
- Classification Report
- Confusion Matrix
- ROC Curve
- Sample Predictions

The complete evaluation is available in:

```
evaluation.ipynb
```

---

## 📌 Model Used

**Feature Extraction**

- TF-IDF Vectorizer

**Classifier**

- Logistic Regression

---

## 📷 Application

The Streamlit application allows users to:

- Enter Hinglish or Manglish text
- Detect Hate / Non-Hate speech
- View prediction instantly

---

## 📚 Future Enhancements

- Improve preprocessing pipeline
- Support additional Indian code-switched languages
- Use transformer-based models (IndicBERT, XLM-R)
- Real-time social media moderation
- Multi-class hate speech classification

---

## 👩‍💻 Author

**Shahista Afreen**

Bachelor of Engineering (Computer Science & Engineering)

Machine Learning | NLP | Python | Streamlit

---

## 📄 License

This project is developed for educational and academic purposes.