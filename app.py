from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.predict import predict_sentiment,model,MODEL_VERSION 
from schema.pydantic_model import Tweet



app = FastAPI(title="Twitter Sentiment Analysis API")


@app.get("/")
def home():
    return {'message':'Welcome to Twitter Sentiment Analysis'}


@app.get("/health")
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }


@app.post("/predict")
def output(tweet: Tweet):
    prediction = predict_sentiment(tweet)
    return JSONResponse(status_code=200, content=prediction)
