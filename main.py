from flask import Flask, render_template


app = Flask(__name__)



@app.route("/")
def home():
    return render_template('home.html', title="Home")


@app.route("/about us")
def about_us():
    return render_template('about us.html', title="About Us")


@app.route("/services")
def services():
    return render_template('services.html', title="Services")


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=int(5000), debug=True)
