from flask import Flask , render_template

app = Flask(__name__,template_folder="../templates")

# Pass the required route to the decorator.
@app.route("/test")
def hello():
    return "Healthy"


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
#just a test that it works










