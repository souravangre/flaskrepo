from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def demosite():
    return render_template ("demosite.html",content="hello ,this is my demosite",list=["tanish","harsh","rajesh"])



if __name__=="__main__":
    app.run(port=1000)