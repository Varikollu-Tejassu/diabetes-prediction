
from flask import Flask,request,render_template
import pickle
app=Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")
@app.route("/predict", methods=['POST'])
def predict():
    if request.method=='POST':
       preg=request.form["preg"]
       gluc=request.form["gluc"]
       bp=request.form["bp"]
       sk=request.form["sk"]
       ins=request.form["ins"]
       bmi=request.form["bmi"]
       dpf=request.form["dpf"]
       age=request.form["age"]
       data=[[int(preg),int(gluc),int(bp),int(sk),int(ins),float(bmi),float(dpf),int(age)]]
       model = pickle.load(open('diabetes1.pkl', 'rb'))
       predi=model.predict(data)[0]
       if predi==1.0:
          x="DIABETIC"
       else:
          x="NON-DIABETIC"
       

       
    return render_template("output.html",predi=x)

if __name__=='__main__':
    app.run(debug=True)