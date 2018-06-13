from flask import Flask,render_tamplate

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("templ.html")
if __name__ == "__main__ " :
    app.run(debug=True)

