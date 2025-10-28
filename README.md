# 🧠 Twitter Sentiment Analysis API

A **Machine Learning-based FastAPI** project that analyzes the **sentiment of tweets** (Positive or Negative).  
The model uses **TF-IDF Vectorization** and a **Logistic Regression classifier** trained on labeled tweet data.

This API is containerized with **Docker**, includes **Pydantic schema validation**, and provides clean endpoints for prediction and health checks.

---

## 📁 Project Structure

├── analyzer/
├── model/
│ ├── predict.py
│ ├── trained_model.sav
│ ├── tfidf_vectorizer.sav
│ └── pycache/
├── schema/
│ ├── pydantic_model.py
│ └── pycache/
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md

---

## 🚀 Features

✅ **FastAPI**-powered RESTful endpoints  
✅ **Preprocessing pipeline** for cleaning tweets  
✅ **TF-IDF + Logistic Regression** ML model  
✅ **Docker support** for easy deployment  
✅ **Swagger UI** documentation at `/docs`  
✅ **Health check** endpoint  
✅ Handles runtime errors gracefully with FastAPI’s `HTTPException`

---

## ⚙️ Tech Stack

| Layer                | Technology                                  |
| -------------------- | ------------------------------------------- |
| **Backend**          | FastAPI                                     |
| **Language**         | Python 3.11                                 |
| **ML Model**         | Scikit-learn (Logistic Regression + TF-IDF) |
| **Data Processing**  | NLTK (stopwords, stemming)                  |
| **Containerization** | Docker                                      |
| **Validation**       | Pydantic                                    |

---

## 🧩 How It Works

### 🧼 1. Preprocessing

Each incoming tweet text is:

-   Lowercased
-   URLs and mentions removed
-   Non-alphabetic characters removed
-   Tokenized, stopwords removed
-   Stemmed using PorterStemmer

### 🤖 2. Prediction

The preprocessed text is transformed via the saved **TF-IDF Vectorizer**, then passed into the **trained Logistic Regression model**.  
The model outputs either `0` (Negative) or `1` (Positive).

### 🧾 3. Response

The API returns:

```json
{
  "tweet": "I love this project!",
  "preprocessed": "love project",
  "sentiment": "Positive"
}


🚀 Live API Access

You can directly access the deployed Sentiment Analysis API without running the project locally.

🔗 Live API URL

👉 https://sentiment-analysis-api-jyef.onrender.com/docs
```
