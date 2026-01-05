from flask import *  
app = Flask(__name__)  
@app.route('/login',methods = ['POST'])  
def login():  
      uname=request.form['uname']  
      passwrd=request.form['pass']  
      if  passwrd=="123":  
          return "Welcome %s" %uname  
if __name__ == '__main__':  
   app.run(debug = True) 