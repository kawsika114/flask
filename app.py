from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    NAME = request.form.get("NAME")
    DEPT = request.form.get("DEPT")
    year = request.form.get("year")
    email = request.form.get("email")
    phoneno = request.form.get("phoneno")
    address = request.form.get("address")


    return f'''Details received successfully: NAME - {NAME},DEPT - {DEPT}, year - {year} email - {email}, phoneno - {phoneno}, address - {address}'''

if __name__ == "__main__":
    app.run(debug=True)

