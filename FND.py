from flask import Flask, render_template, request
from MainCode 

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']
        pred = Project_Allocation(message)
        print(pred)
        return render_template('home.html', prediction=pred)
    else:
        return render_template('home.html', prediction="Something went wrong")

if __name__ == '__main__':
    app.run(debug=True)