import re
import nltk
import pickle
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from fastapi import HTTPException
from schema.pydantic_model import Tweet



nltk.download('stopwords', quiet=True)
all_stopwords = stopwords.words('english')
ps = PorterStemmer()


try:
    with open('model/trained_model.sav', 'rb') as f:
        model = pickle.load(f)

    with open('model/tfidf_vectorizer.sav', 'rb') as v:
        vectorizer = pickle.load(v)
except FileNotFoundError:
    raise RuntimeError("Model or vectorizer file not found. Please check your paths.")

MODEL_VERSION = "1.0.1"


def preprocess(text: str) -> str:
    text = text.lower()
    text = re.sub(r"http\S+", "", text)        # remove URLs
    text = re.sub(r"@\w+", "", text)           # remove mentions
    text = re.sub(r"[^a-zA-Z\s]", "", text)    # remove punctuation
    text = text.split()
    text = [ps.stem(word) for word in text if word not in all_stopwords]
    return " ".join(text)


def predict_sentiment(tweet: Tweet):
    try:
        clean_text = preprocess(tweet.text)
        features = vectorizer.transform([clean_text])
        prediction = model.predict(features)[0]
        sentiment = "Negative" if prediction == 0 else "Positive"
        # probabilities = model.predict_proba(features)[0] 
        # confidence = float(probabilities[prediction])

        return {
            "tweet": tweet.text,
            "preprocessed": clean_text,
            "sentiment": sentiment,
            # "confidence": round(confidence, 4)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during prediction: {str(e)}")