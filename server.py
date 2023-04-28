from flask import Flask

app = Flask(__name__)

# Pass the required route to the decorator.
@app.route("/test")
def hello():
    return "Healthy"


@app.route("/")
def index():
    return "Elo Wald!!"


if __name__ == "__main__":
    app.run(debug=True)
#just a test that it works










