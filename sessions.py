from flask import Flask,session,redirect,request,render_template,g,url_for

app = Flask(__name__)

app.secret_key='abcd'
@app.route('/',methods=["post","get"])
def login():
    if request.method=='post':
       

        if request.form["password"]=='password':
            session['user']=request.form['username']
            return redirect(url_for('afterlogin'))
    return render_template('loginpage.html')  

@app.route('/afterlogin')
def afterlogin(): 
    if g.user:
        return render_template('afterlogin.html', user=session['user'])
    return redirect(url_for('loginpage'))

@app.before_request
def before_request():
    g.user=None

    if 'user' in session:
        g.user=session['user']

@app.route('/dropsession')
def dropsession():
    session.pop('user',None)
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
