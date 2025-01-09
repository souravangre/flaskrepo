from flask import Flask ,render_template,redirect,url_for,request,flash
from flask_sqlalchemy import SQLAlchemy                                             # importing modules
from flask_login import LoginManager,login_user ,logout_user
from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__)                                                               # setting app

app.secret_key="sourav"                                                             # setting a secret key
                                                                          

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'                       # settingg DB configuration
db=SQLAlchemy(app)

class Users(db.Model):                                                              # creating a user model to store data
    id=db.Column(db.Integer,primary_key=True)    
    email=db.Column(db.String(50),unique=True,nullable=False)
    password_hash=db.Column(db.String(200),nullable=False)
   

    def set_password(self,password):
        self.password_hash=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)    

class comments(db.Model):                                                           # creating a user model to store data
    id=db.Column(db.Integer,primary_key=True) 
    name=db.Column(db.String(50),nullable=False)   
    email=db.Column(db.String(50),nullable=False)
    message=db.Column(db.String(250),nullable=False)
                                                                      
with app.app_context():                                                             # save the DB         
 db.create_all() 

login_manager=LoginManager()                                                        # setting up login manager configs
login_manager.init_app(app)

@login_manager.user_loader                                                          # adding user loader which loads the data in Db
def user_loader(user_id):
    return user_id.query.get(user_id)
 


@app.route('/')                                                                     # Route for home
def home():                                                                                 
    return render_template("arthome.html")

@app.route('/signup',methods=["GET","POST"])                                        # route for signup
def signup():
     if request.method=="POST":
                                                                                    # create a user
          email=request.form["email"]
          password_hash=generate_password_hash(request.form["password"])

          user=Users.query.filter_by(email=email).first()
          if user:
              flash("Email already exists.Please login")
              return redirect(url_for("signup"))

          user=Users(email=email,password_hash=password_hash)

          db.session.add(user)
          db.session.commit()
          return redirect(url_for("login"))
     else:
         return render_template("signup.html")
      
            
@app.route('/login',methods=['GET','POST'])                                          # route for login 
def login():
   
    if request.method=="POST": 
                                                        #login user if valid
        email=request.form["email"]
        password=request.form["password"]
        user= Users.query.filter_by(email=email).first()
        if user is not None and check_password_hash(user.password_hash,password):
             return redirect(url_for("blog")) 
        else:
            flash("Please check your login details and try again")
            return redirect(url_for("login"))
         
    return render_template('login.html')
       
       
         
@app.route('/blog',methods=["GET","POST"])  
                                       # route for blog
def blog():
    if request.method=="POST":                                                       # user messages in blog
          name=request.form["cname"]
          email=request.form["cemail"]
          message=request.form["ctext"]
          new_comment=comments(name=name,email=email,message=message)
          db.session.add(new_comment)
          db.session.commit()
          flash("Submitted !")
    return render_template("blog.html")



@app.route('/logout')                                                                # route for logout
def logout():
    logout_user()
    return render_template("arthome.html")

if __name__=="__main__":                                                             # main app running instance
     app.run(debug=True, port=5000)
  