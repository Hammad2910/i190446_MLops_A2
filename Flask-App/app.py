from contextlib import _RedirectStream
from flask import Flask, render_template, url_for

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

from flask import request
from flask import redirect
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd


with open('linear_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/submit-form', methods=['POST'])
def submit_form():
    open_val = request.form.get('open')
    high = request.form.get('high')
    low = request.form.get('low')
    volume = request.form.get('volume')
    print("Open: ", open_val, "High: ", high, "Low: ", low, "Volume: ", volume)
    data = {"Open": open_val, "High": high, "Low": low, "Volume": volume}
   
    # Convert the input values to a NumPy array
    input_vals = np.array([[open_val, high, low, volume]])
    #my_dataframe = pd.DataFrame(input_vals)

    # create a DataFrame from the numpy array with column names
    df = pd.DataFrame(input_vals, columns=['Open', 'High', 'Low', 'Volume'])

    with open('linear_regression_model.pkl', 'rb') as f:
        model = pickle.load(f)
     # Make a prediction using the loaded model
    prediction = model.predict(df)

    # Return the prediction as a string
    predicted_closing = prediction[0];
    data["Closing"] = predicted_closing
    
    return render_template('prediction.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)