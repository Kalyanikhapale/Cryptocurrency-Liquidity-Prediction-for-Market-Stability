from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load("liquidity_model_optimized.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        prediction = model.predict([features])[0]
        return render_template("index.html", prediction_text=f"Predicted Liquidity Ratio: {prediction:.4f}")
    except:
        return render_template("index.html", prediction_text="Invalid input. Please enter numeric values.")

if __name__ == '__main__':
    app.run(debug=True)
