# SheSecure – AI-Based Women Safety Prediction System

SheSecure is an end-to-end machine learning web application that predicts women safety risk levels using crime data, enhanced with user sentiment analysis for contextual understanding.

---

## Overview

The system combines two components:

- Risk Prediction using crime statistics  
- Sentiment Analysis based on user input  

This provides a more realistic safety assessment by combining data with human perception.

---

## Features

- State-based risk prediction  
- Custom input mode for simulation  
- NLP-based sentiment classification (Safe / Unsafe)  
- Web interface built using Flask  
- Map-based visualization of risk levels  

---

## Methodology

### Machine Learning
- Input features: Rape, Kidnapping, Dowry Deaths, Assault, Minor Cases, Domestic Violence, Trafficking  
- Model: Random Forest Classifier  
- Output: Low, Medium, High risk levels  

### NLP
- TF-IDF vectorization  
- Logistic Regression classifier  
- Output: Safe / Unsafe  

---

## System Flow

Crime Data → ML Model → Risk Level  
User Input → NLP Model → Sentiment  

Final output combines both predictions.

---

## Modes

- State Mode: Uses preprocessed real data  
- Manual Mode: Allows custom input for testing scenarios  

---

## Tech Stack

- Python, Flask  
- Scikit-learn  
- NumPy, Pandas  
- HTML, CSS  
- Folium  

---

## Project Structure

SheSecure/  
├── app.py  
├── ml_model.pkl  
├── nlp_model.pkl  
├── vectorizer.pkl  
├── templates/  
├── static/  

---

## Run Locally

git clone https://github.com/Siddhi22/SheSecure.git
cd SheSecure  

pip install flask scikit-learn numpy pandas  

python app.py  

Open in browser:  
http://127.0.0.1:5000/

---

## Future Improvements

- Real-time data integration  
- Advanced NLP models (LSTM / BERT)  
- Deployment on cloud platforms  

---

## Summary

This project demonstrates an integrated approach combining machine learning, NLP, and web development to build a practical safety prediction system.
