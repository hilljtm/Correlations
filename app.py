from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gold')
def gold():
    return render_template('gold.html')

@app.route('/spindex')
def spindex():
    return render_template('spindex.html')

@app.route('/faang')
def faang():
    return render_template ('faang.html')

    
if __name__ == '__main__':
    app.run(debug=True)
