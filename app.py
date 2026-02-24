
from flask import Flask, render_template, request
import numpy as np
import joblib

# Load trained model
model = joblib.load("startup_success_model.pkl")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        final_features = np.array([features])

        prediction = model.predict(final_features)

        if prediction[0] == 1:
            output = "Startup Will be SUCCESSFUL"
        else:
            output = "Startup May FAIL"

        return render_template("index.html", prediction_text=output)

    except:
        return render_template("index.html", prediction_text="Error in Input Data")

if __name__ == "__main__":
    app.run(debug=True)
