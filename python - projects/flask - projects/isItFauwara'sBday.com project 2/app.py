from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route('/')
def home():
    birthDate = date(2001,11,21)
    today = date.today()
    status = birthDate.month == today.month and birthDate.day == today.day
    return render_template('index.html',status = status)

if __name__ == "__main__":
    app.run(debug = True)