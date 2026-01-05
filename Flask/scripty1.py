from flask import Flask  

app = Flask(__name__) #creating the Flask class object   

@app.route('/') #decorator    

def home():  

    return "hello, this is our first flask website";  

if __name__ =='__main__':  

    app.run(debug = True)  

 