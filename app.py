from flask import Flask, render_template, request, session

app = Flask(__name__)
# The session key secures the session cookies so that they cannot be modified
app.secret_key = "djfd99dfdjks9fdjs"

# Main that takes input and puts it into the session object with "username" as a key
@app.route("/", methods=["GET", "POST"])
def input_username():
    if request.method == 'POST':
        username = request.form['username']
        session["Username"] = username
    print(session)
    return render_template('hello.html')

@app.route("/see_username", methods=["GET", "POST"])
def see_username():
    if session["Username"]:
        return render_template("get.html", user=session["Username"])
    else:
        return render_template("get.html", user="Not Found")


