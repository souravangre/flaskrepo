from flask import Flask ,render_template,redirect,url_for

app = Flask(__name__)
INFO=[
    {
        "id":1,
        "name":"art1",
        "price":"1000$"
    },
     {
        "id":2,
        "name":"art2",
        "price":"2000$"
    },
     {
        "id":3,
        "name":"art3",
        "price":"3000$"
    },
     {
        "id":4,
        "name":"art4",
        "price":"4000$"
    }
]
@app.route('/')
def hello_world():
    return ("hello")
 
@app.route('/art')
def art():
    return render_template("art.html",info=INFO)
 

if __name__=="__main__":
    app.run(debug=True, port=2000)
