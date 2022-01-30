from flask import Flask, render_template, request
from create_qr import create_qr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('website.html')

@app.route('/render', methods=['GET', 'POST'])
def index2():
    hash = request.args.get('hash')
    create_qr(hash)
    return render_template("website.html", qr = "static/images/qr.png")

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)