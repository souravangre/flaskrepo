from flask import Flask,render_template,redirect,url_for
import sqlalchemy

app=Flask(__name__)

@app.route('/')
def page():
    return render_template("demoapp.html")

if __name__=="__main__":
    app.run(debug=True)