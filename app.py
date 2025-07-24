from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
  return "<h2>Hello, World!</h2>"

@app.route("/home")
def home():
  return render_template("home.html")


if __name__ == "__main__":
  # print("This is the main module.")
  app.run(host='0.0.0.0', port=8080, debug=True)
