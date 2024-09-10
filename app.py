from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('Mango.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    area = float(request.form['area'])
    prediction = model.predict([[area]])
    return render_template('index.html', prediction_text=f'Estimated Price in Rupees = {prediction[0]:.2f}')

if __name__ == "__main__":
    app.run(debug=True, port= 8000)
