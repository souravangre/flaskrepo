from flask import Flask,render_template,redirect ,url_for,request,session
from datetime import timedelta

app=Flask(__name__)
app.secret_key ="sourav"
app.permanent_session_lifetime=timedelta(minutes=1)

@app.route("/")
def index1():
    return render_template("index1.html")


@app.route("/login1",methods=["POST","GET"])
def login1():
    if request.method=="POST":
        session.permanent=False
        user=request.form["name"]
        session["user"]=user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
    return render_template("login1.html")

@app.route("/user")
def user():
    if "user" in session :
        user=session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect (url_for("login1"))
    
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login1"))    


if __name__=="__main__":
    app.run(debug=True)