import pickle

from flask import Flask, render_template, request
app = Flask(__name__)
model = pickle.load(open('D:\\b tech\\vap\\models\\house_price_model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route("/predict", methods=["POST"])
def predict():
    area = float(request.form.get("area"))
    prediction = model.predict([[area]])
    return render_template('index.html', prediction=f'{prediction[0]:.2f}')

if __name__ == "__main__":
    app.run(debug=True)