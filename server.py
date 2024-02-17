from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "C0d!ng !$ fun"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    session['count'] = request.form['']
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)