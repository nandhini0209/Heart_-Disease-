# Heart Risk AI — Heart Disease Prediction Web App

A machine learning web application that predicts the likelihood of heart disease
based on 13 clinical features using a Random Forest classifier.

## Features
- Predicts heart disease risk from 13 clinical inputs
- Displays risk probability as a percentage
- Shows input summary after prediction
- Mobile-responsive, medical-themed UI
- Deployable on Render.com

## Project Structure
```
Heart_disease/
├── app.py
├── train_model.py
├── model.pkl
├── requirements.txt
├── Procfile
├── runtime.txt
├── .gitignore
├── README.md
├── dataset/
│   └── heart.csv
├── templates/
│   ├── index.html
│   ├── result.html
│   └── about.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── script.js
```

## Setup & Run Locally

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Train the model:
   ```bash
   python train_model.py
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open `http://127.0.0.1:5000` in your browser

## Dataset
UCI Heart Disease Dataset (Cleveland Clinic Foundation)
https://archive.ics.uci.edu/dataset/45/heart+disease

## Disclaimer
For educational purposes only. Not a substitute for medical advice.


