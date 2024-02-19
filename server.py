from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "C0d!ng !$ fun"

@app.route('/')
def home():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/add')
def add():
    if 'count' in session:
        session['count'] = session['count'] + 1
    else:
        session['count'] += 1
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 0
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)