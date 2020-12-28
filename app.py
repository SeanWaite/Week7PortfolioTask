from flask import Flask, render_template, request, redirect

app = Flask(__name__)

USERNAME = 'Blank'
EMAIL = 'Blank'
PASSWORD = 'Blank'

@app.route('/')
def easyDoesIt():

    user = 'Sean'
    title = 'Drink'
    drinks = [
        {'Water':'https://en.wikipedia.org/wiki/Water'},
        {'Green Tea':'https://en.wikipedia.org/wiki/Green_tea'},
        {'Beer':'https://en.wikipedia.org/wiki/Beer'},
        {'Whisky':'https://en.wikipedia.org/wiki/Whisky'}
        ]

    return render_template("footer.html", title=title, user=user, drinks=drinks)
    #return "<h1>Easy does it!</h1>"

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        req = request.form
        print(req)

        global USERNAME
        global EMAIL
        global PASSWORD

        USERNAME = req.get("username")
        EMAIL = req.get("email")
        PASSWORD = req.get("password")

        print("username:" + USERNAME)
        print("email:" + EMAIL)
        print("password:" + PASSWORD)

        missing = list()

        for field, value in req.items():
            if value == "":
                missing.append(field)

        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("sign_up.html", feedback=feedback)

        return render_template("sign_up_details.html",
                               user=USERNAME,
                               email=EMAIL,
                               password=PASSWORD)

    return render_template("sign_up.html")

@app.route("/sign-up-details")
def sign_up_detials():
    return render_template("sign_up_details.html",
                           user=USERNAME,
                           email=EMAIL,
                           password=PASSWORD)

if __name__ == '__main__':
    app.run()
