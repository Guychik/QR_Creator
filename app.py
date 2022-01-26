from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('website.html')

@app.route('/render', methods=['GET', 'POST'])
def index2():
    hash = request.args.get('hash')
    return render_template("website.html", qr = 'https://api.qrserver.com/v1/create-qr-code/?data={}&amp;size=500x500'.format(hash))

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)