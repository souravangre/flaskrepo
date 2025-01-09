from flask import Flask,render_template,redirect ,url_for,request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        name=request.form["nm"]
        return redirect(url_for("user",usr=name))
    return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"



if __name__=="__main__":
    app.run(debug=True)