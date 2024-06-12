from flask import Flask,render_template,redirect,url_for,request

app=Flask(__name__)

@app.route("/home")
def home(name):
    return ("hello",name)

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user=request.form["username"]
        return redirect(url_for("home",name=user))
    else:
        user=request.args.get("username")
        return redirect(url_for("home",name=user))
    

if __name__=="__main__":
    app.run(debug=True ,port=3000)