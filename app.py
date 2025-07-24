from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# all generated through replit AI
@app.route("/")
@app.route("/home")
def home():
  return render_template("home.html")


@app.route("/about")
def about():
  # return "<h1>About Page</h1>"
  return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
  if request.method == "POST":
    # Handle form submission here
    # You can process the form data, send emails, etc.
    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")

    # For now, just print the data (you can implement email sending later)
    print(f"Contact form submitted: {name}, {email}, {subject}")

    # You could redirect to a thank you page or show a success message
    return redirect("/contact")

  return render_template("contact.html")


if __name__ == "__main__":
  # print("This is the main module.")
  app.run(host='0.0.0.0', port=8080, debug=True)
