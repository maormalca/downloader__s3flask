from flask import Flask, render_template,request
import backend
app = Flask(__name__)
@app.route('/',methods=["GET","POST"])
def hello():
    if request.method=="POST":
        text = request.form['flabel']
        try:
            backend.searchNdownolad(text)
            return render_template("sucsess.html")
        except:
            return render_template("error.html")    
    else:
        return render_template("frontend.html")
if __name__ == "__main__":
        app.run(debug=True,port=8082,host="0.0.0.0")


        