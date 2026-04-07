from flask import Flask, render_template, request
import joblib
import numpy as np
import pickle

app = Flask(__name__)

# Load models
ml_model = joblib.load("ml_model.pkl")
nlp_model = pickle.load(open("nlp_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# State-wise data (expanded)
state_data = {
    "Delhi": [1200,1000,200,4000,300,2500,100],
    "Maharashtra": [1000,900,180,3500,250,2000,80],
    "Karnataka": [700,600,100,2000,150,1500,50],
    "Tamil Nadu": [650,500,90,1800,120,1400,40],
    "Uttar Pradesh": [1500,1200,250,4500,350,3000,120],
    "Bihar": [900,800,150,2500,200,1800,60],
    "Rajasthan": [850,700,140,2300,180,1700,55],
    "West Bengal": [800,750,130,2200,170,1600,50],
    "Madhya Pradesh": [950,850,160,2600,210,1900,65],
    "Gujarat": [600,500,80,1800,120,1300,40]
}

# Send states to UI
@app.route('/')
def home():
    return render_template("index.html", states=list(state_data.keys()))

@app.route('/predict', methods=['POST'])
def predict():

    mode = request.form['mode']

    # MODE SWITCH
    if mode == "state":
        state = request.form['state']
        data = state_data[state]
    else:
        state = "Custom Input"
        data = [
            float(request.form['rape']),
            float(request.form['kidnapping']),
            float(request.form['dowry']),
            float(request.form['assault']),
            float(request.form['minor']),
            float(request.form['dv']),
            float(request.form['trafficking'])
        ]

    # ML prediction
    prediction = ml_model.predict([data])[0]
    risk = ["Low", "Medium", "High"][prediction]

    # NLP prediction
    text = request.form['text']
    vec = vectorizer.transform([text])
    sentiment_pred = nlp_model.predict(vec)[0]
    sentiment = "Safe" if sentiment_pred == 1 else "Unsafe"

    return render_template("result.html",
                           state=state,
                           risk=risk,
                           sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)