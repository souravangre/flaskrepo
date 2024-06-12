from flask import Flask,render_template,redirect,url_for,request

app=Flask(__name__)

@app.route("/")
def home():
    return ("hello")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user=request.form["username"]
        return redirect(url_for("userpage",name=user))
    else:
        return render_template("form.html")
    
@app.route('/name')
def userpage(name):
    return ("Hii,this is a default page for",name)    

if __name__=="__main__":
    app.run(debug=True ,port=3000)