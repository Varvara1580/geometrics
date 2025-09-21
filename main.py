from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/app')
def app_sait():
    return render_template('app.html')

@app.route('/3')
def f_sait():
    return render_template('3.html')

if __name__ == '__main__':
    app.run()