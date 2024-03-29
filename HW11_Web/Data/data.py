
from flask import Flask,render_template, request
import pandas as pd
import numpy as np
app = Flask(__name__)
 
@app.route("/")
def index():
        df = pd.read_csv("./Resources/cities.csv")
        return render_template("index_data.html", data=df.head(5).to_html())
 
if __name__ == "__main__":
    app.run()