
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Configuration data for the website
SITE_CONFIG = {
    'personal_info': {
        'full_name': 'Pritish Togare',
        'title': 'Full Stack Developer & Problem Solver',
        'description': 'I create beautiful, functional, and user-friendly web applications using modern technologies. Passionate about clean code, innovative solutions, and continuous learning.',
        'email': 'pritish.togare@example.com',
        'phone': '+1 (555) 123-4567',
        'location': 'Your City, Country'
    },
    'skills': [
        {
            'icon': 'fab fa-python',
            'name': 'Python',
            'description': 'Flask, Django, FastAPI'
        },
        {
            'icon': 'fab fa-js-square',
            'name': 'JavaScript',
            'description': 'React, Node.js, Express'
        },
        {
            'icon': 'fas fa-database',
            'name': 'Databases',
            'description': 'PostgreSQL, MongoDB, Redis'
        },
        {
            'icon': 'fab fa-git-alt',
            'name': 'DevOps',
            'description': 'Git, Docker, CI/CD'
        }
    ],
    'projects': [
        {
            'icon': 'fas fa-laptop-code',
            'title': 'Web Application',
            'description': 'A full-stack web application built with Flask and React',
            'link': '#'
        },
        {
            'icon': 'fas fa-mobile-alt',
            'title': 'Mobile App',
            'description': 'Cross-platform mobile application with modern UI/UX',
            'link': '#'
        },
        {
            'icon': 'fas fa-chart-line',
            'title': 'Data Analytics',
            'description': 'Data visualization and analytics dashboard',
            'link': '#'
        }
    ],
    'social_links': {
        'github': 'https://github.com/yourusername',
        'linkedin': 'https://linkedin.com/in/yourusername',
        'twitter': 'https://twitter.com/yourusername',
        'instagram': 'https://instagram.com/yourusername'
    },
    'experience': [
        {
            'title': 'Senior Full Stack Developer',
            'company': 'Tech Company Inc.',
            'period': '2022 - Present',
            'description': 'Leading development of scalable web applications using modern technologies.'
        },
        {
            'title': 'Software Developer',
            'company': 'StartUp Co.',
            'period': '2020 - 2022',
            'description': 'Developed and maintained multiple web applications using Python and JavaScript.'
        },
        {
            'title': 'Computer Science Degree',
            'company': 'University Name',
            'period': '2016 - 2020',
            'description': 'Bachelor of Science in Computer Science with focus on software engineering.'
        }
    ],
    'values': [
        {
            'icon': 'fas fa-code',
            'title': 'Clean Code',
            'description': 'Writing maintainable, readable, and efficient code that stands the test of time.'
        },
        {
            'icon': 'fas fa-lightbulb',
            'title': 'Innovation',
            'description': 'Always exploring new technologies and creative solutions to complex problems.'
        },
        {
            'icon': 'fas fa-users',
            'title': 'Collaboration',
            'description': 'Working effectively with teams to deliver exceptional results.'
        }
    ]
}

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
