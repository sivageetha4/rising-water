Flood_Prediction/
│
├── app.py
├── floods.save
├── transform.save
├── flood.csv
│
├── templates/
│      │
│      ├── home.html
│      ├── index.html
│      ├── chance.html
│      └── no_chance.html
│
└── static/
       │
       ├── style.css
       └── images/
       from flask import Flask, render_template, request
from joblib import load
import pandas as pd
app = Flask(__name__)
model = load("floods.save")
scaler = load("transform.save")
@app.route("/")
def home():
    return render_template("home.html")
    http://127.0.0.1:5000/
    @app.route("/Predict")
def predict_page():
    return render_template("index.html")
    @app.route("/predict", methods=["POST"])
def predict():

    Temp = float(request.form["Temp"])
    Humidity = float(request.form["Humidity"])
    Cloud_Cover = float(request.form["Cloud Cover"])
    Annual = float(request.form["ANNUAL"])
    Jan_Feb = float(request.form["Jan-Feb"])
    Mar_May = float(request.form["Mar-May"])
    Jun_Sep = float(request.form["Jun-Sep"])
    Oct_Dec = float(request.form["Oct-Dec"])
    AvgJune = float(request.form["avgjune"])
    Sub = float(request.form["sub"])

    data = pd.DataFrame([[Temp,
                          Humidity,
                          Cloud_Cover,
                          Annual,
                          Jan_Feb,
                          Mar_May,
                          Jun_Sep,
                          Oct_Dec,
                          AvgJune,
                          Sub]],
                        columns=[
                            "Temp",
                            "Humidity",
                            "Cloud Cover",
                            "ANNUAL",
                            "Jan-Feb",
                            "Mar-May",
                            "Jun-Sep",
                            "Oct-Dec",
                            "avgjune",
                            "sub"
                        ])

    data = scaler.transform(data)

    prediction = model.predict(data)

    if prediction[0] == 1:
        return render_template("chance.html")
    else:
        return render_template("no_chance.html")
        if __name__ == "__main__":
    app.run(debug=True)
    http://127.0.0.1:5000/
    <!DOCTYPE html>
<html>

<head>
    <title>Flood Prediction</title>
</head>

<body>

<h1>Rising Waters</h1>

<h2>Flood Prediction System</h2>

<a href="/Predict">
<button>Start Prediction</button>
</a>

</body>

</html>
<!DOCTYPE html>
<html>

<head>
    <title>Prediction</title>
</head>

<body>

<h2>Enter Weather Details</h2>

<form action="/predict" method="POST">

<input type="number" step="any" name="Temp" placeholder="Temperature"><br><br>

<input type="number" step="any" name="Humidity" placeholder="Humidity"><br><br>

<input type="number" step="any" name="Cloud Cover" placeholder="Cloud Cover"><br><br>

<input type="number" step="any" name="ANNUAL" placeholder="Annual Rainfall"><br><br>

<input type="number" step="any" name="Jan-Feb" placeholder="Jan-Feb"><br><br>

<input type="number" step="any" name="Mar-May" placeholder="Mar-May"><br><br>

<input type="number" step="any" name="Jun-Sep" placeholder="Jun-Sep"><br><br>

<input type="number" step="any" name="Oct-Dec" placeholder="Oct-Dec"><br><br>

<input type="number" step="any" name="avgjune" placeholder="Average June"><br><br>

<input type="number" step="any" name="sub" placeholder="Sub"><br><br>

<input type="submit" value="Predict">

</form>

</body>

</html>
<!DOCTYPE html>
<html>

<head>
<title>Flood Alert</title>
</head>

<body>

<h1>⚠ Flood Expected</h1>

<h2>Please Take Necessary Precautions.</h2>

<a href="/">Home</a>

</body>

</html>
<!DOCTYPE html>
<html>

<head>
<title>No Flood</title>
</head>

<body>

<h1>✅ No Flood Expected</h1>

<h2>Weather Conditions are Safe.</h2>

<a href="/">Home</a>

</body>

</html>
User Opens Website
        │
        ▼
Home Page (/)
        │
        ▼
Prediction Page (/Predict)
        │
        ▼
Enter Weather Details
        │
        ▼
Submit Form
        │
        ▼
Flask Receives POST Request
        │
        ▼
Create DataFrame
        │
        ▼
Apply StandardScaler
        │
        ▼
Load ML Model
        │
        ▼
Predict Flood
        │
        ├──────────────┐
        ▼              ▼
Flood = 1         Flood = 0
        ▼              ▼
chance.html   no_chance.html
if __name__ == "__main__":
    app.run(debug=True)
    