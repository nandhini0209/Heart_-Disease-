 ============================================================
# app.py - Flask Backend for Heart Disease Prediction App
# ============================================================

from flask import Flask, render_template, request
import pickle
import numpy as np

# Create the Flask app instance
app = Flask(__name__)

# ============================================================
# Load the trained model and scaler from model.pkl
# ============================================================
with open('model.pkl', 'rb') as f:
    model, scaler = pickle.load(f)

# ============================================================
# Home Route - Show the prediction form
# ============================================================
@app.route('/')
def index():
    return render_template('index.html')

# ============================================================
# About Route - Show the about page
# ============================================================
@app.route('/about')
def about():
    return render_template('about.html')

# ============================================================
# Predict Route - Handle form submission and make prediction
# ============================================================
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect all 13 input values from the form
        features = [
            float(request.form['age']),
            float(request.form['sex']),
            float(request.form['cp']),
            float(request.form['trestbps']),
            float(request.form['chol']),
            float(request.form['fbs']),
            float(request.form['restecg']),
            float(request.form['thalach']),
            float(request.form['exang']),
            float(request.form['oldpeak']),
            float(request.form['slope']),
            float(request.form['ca']),
            float(request.form['thal']),
        ]

        # Convert to numpy array and reshape for the model
        input_array = np.array(features).reshape(1, -1)

        # Scale the input using the saved scaler
        input_scaled = scaler.transform(input_array)

        # Make prediction (0 = no disease, 1 = disease)
        prediction = model.predict(input_scaled)[0]

        # Get probability percentage
        probability = round(model.predict_proba(input_scaled)[0][1] * 100, 2)

        # Build input summary dictionary for the result page
        input_data = {
            'Age': request.form['age'],
            'Sex': 'Male' if request.form['sex'] == '1' else 'Female',
            'Chest Pain Type': request.form['cp'],
            'Resting Blood Pressure': request.form['trestbps'],
            'Cholesterol': request.form['chol'],
            'Fasting Blood Sugar': request.form['fbs'],
            'Resting ECG': request.form['restecg'],
            'Max Heart Rate': request.form['thalach'],
            'Exercise Induced Angina': request.form['exang'],
            'ST Depression (Oldpeak)': request.form['oldpeak'],
            'Slope': request.form['slope'],
            'Number of Vessels': request.form['ca'],
            'Thal': request.form['thal'],
        }

        # Render the result page with prediction data
        return render_template('result.html',
                               prediction=int(prediction),
                               probability=probability,
                               input_data=input_data)

    except Exception as e:
        # If something goes wrong, show an error message
        return render_template('index.html', error=f"Error: {str(e)}")


if __name__ == '__main__':
    app.run(debug=True)
