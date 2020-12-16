from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classes/<int:id>')

def classes(id):
    return render_template('classe.html',ids = id)

if __name__ == "__main__":
    app.run(debug=True)
