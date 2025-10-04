from flask import Flask, render_template, request
import numpy as np
import joblib
import os

# Initialize Flask app
app = Flask(__name__)

# Load trained pipeline model
MODEL_PATH = os.path.join("app", "models", "best_model.pkl")
model = joblib.load(MODEL_PATH)

# Emoji mapping for Iris species
emoji_map = {
    "Iris-setosa": "🌼",
    "Iris-versicolor": "🌸",
    "Iris-virginica": "🌺"
}

@app.route("/", methods=["GET", "POST"])
def index():
    prediction_text = None  # default: no result

    if request.method == "POST":
        try:
            # Collect inputs from form
            sepal_length = float(request.form.get("Sepal_Length", 0))
            sepal_width = float(request.form.get("Sepal_Width", 0))
            petal_length = float(request.form.get("Petal_Length", 0))
            petal_width = float(request.form.get("Petal_Width", 0))

            # Prepare input for prediction
            features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

            # Make prediction
            prediction = model.predict(features)[0]
            emoji = emoji_map.get(prediction, "🌸")  # default if not found
            prediction_text = f"{emoji} The predicted Iris species is: <b>{prediction}</b>"

        except Exception as e:
            prediction_text = f"Error: {str(e)}"

    # On GET request, prediction_text will be None → no result displayed
    return render_template("index.html", prediction_text=prediction_text)


if __name__ == "__main__":
    app.run(debug=True)
