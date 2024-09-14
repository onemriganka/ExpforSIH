from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the model (ensure the model file 'Mango.pkl' exists in the project directory)
model = joblib.load('Mango.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input value from the form (named "price" in your HTML)
        price = float(request.form['price'])
        
        # Predict using the model
        prediction = model.predict([[price]])
        
        # Render the result on the page
        return render_template('index.html', prediction_text=f'Estimated Price in Rupees = {prediction[0]:.2f}')
    
    except KeyError as e:
        return f"KeyError: The form field '{e.args[0]}' is missing.", 400
    
    except Exception as e:
        return f"An error occurred: {e}", 500

if __name__ == "__main__":
    app.run(debug=True, port=8000)
