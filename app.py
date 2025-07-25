from flask import Flask, render_template, request, redirect
from info import SITE_CONFIG

app = Flask(__name__)

# Configuration data for the website


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",
                           personal_info=SITE_CONFIG['personal_info'],
                           skills=SITE_CONFIG['skills'],
                           projects=SITE_CONFIG['projects'],
                           social_links=SITE_CONFIG['social_links'])


@app.route("/about")
def about():
    return render_template("about.html",
                           personal_info=SITE_CONFIG['personal_info'],
                           experience=SITE_CONFIG['experience'],
                           values=SITE_CONFIG['values'],
                           social_links=SITE_CONFIG['social_links'])


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Handle form submission here
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        # For now, just print the data (you can implement email sending later)
        print(f"Contact form submitted: {name}, {email}, {subject}")
        print(f"Message: {message}")

        # You could redirect to a thank you page or show a success message
        return redirect("/contact")

    return render_template("contact.html",
                           personal_info=SITE_CONFIG['personal_info'],
                           social_links=SITE_CONFIG['social_links'])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
