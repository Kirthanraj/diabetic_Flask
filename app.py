import joblib
from flask import Flask,render_template,request   
app=Flask(__name__)

@app.route('/')
def base():
    return render_template('home.html')

@app.route('/predict',methods=['post']) 
def predict():

    model=joblib.load("dibatic_81.pkl")
    preg= request.form.get('preg')
    pres= request.form.get('pres')
    plas= request.form.get('plas')
    skin= request.form.get('skin')
    test= request.form.get('test')
    mass= request.form.get('mass')
    pedi= request.form.get('pedi')
    age= request.form.get('age')
    print(preg,plas,pres,skin,test,mass,pedi,age)
    
    output=model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])
    if output[0] == 0:
     data='person is not dibatic' 
    else:
     data='person is dibatic'
    return render_template('predict.html',data=data)

    if __name__=="__main__"
      app.run(debug=True)