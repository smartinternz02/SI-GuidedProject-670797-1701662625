from flask import Flask,request,render_template
import pickle
import pandas as pd
import numpy as np
app=Flask(__name__)
model=pickle.load(open(r'rfc_coffee.pkl','rb'))
@app.route('/')
@app.route('/home',methods=["GET","POST"])
def home():
  return render_template('index.html')


@app.route('/predict',methods=["GET","POST"])
def predict():
  return render_template('predict.html')


@app.route('/output',methods=["GET","POST"])
def output():
  input_feature=[float(x) for x in request.form.values() if x]
  try:
    # Your code block where OSError is raised
    print(input_feature)
  except OSError as e:
    print(f"OSError occurred: {e}")
    # Other error handling steps if needed
  names=['Aroma','Flavor','Aftertaste','Acidity','Body','Balance','Uniformity','Category One Defects','Quakers','Category Two Defects','Color_encoded']

  if len(input_feature) == len(names):
    data = pd.DataFrame([input_feature], columns=names)
    print(data)
        # Further processing or returning the data as needed
   
  
  prediction=model.predict(data)
  print(prediction)
  out=prediction[0]
  return render_template("output.html",output=np.round(out))
if __name__=="__main__":
    app.run(debug=True)