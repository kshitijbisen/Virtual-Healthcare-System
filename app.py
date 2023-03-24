
from flask import Flask, render_template, request, url_for
import numpy as np
import pickle

model=pickle.load(open(r'C:\Users\Kshitij\OneDrive\Desktop\edi\dbfinal.pkl','rb'))
# model2=pickle.load(open(r'C:\Users\Kshitij\OneDrive\Desktop\edi\hdfinal.pkl','rb'))
app=Flask(__name__,
            static_url_path='', 
            static_folder='templates')

# @app.route('/')
# def man():
#     return render_template("edi.html")

# @app.route('/nutrition')
# def nutri():
#     return render_template("nutrition.html")

# @app.route('/chestedi')
# def chestedi():
#     return render_template("chestedi.html")

# @app.route('/ddf')
# def ddf():
#     return render_template("ddf.html")
# @app.route('/hd')
# def hd():
#     return render_template("hd.html")  

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
    HighBP=request.form['HighBP']
    HighChol =request.form['HighChol']
    BMI =request.form['BMI']
    Smoker =request.form['Smoker']
    Stroke=request.form['Stroke']
    HeartDiseaseorAttack =request.form['HeartDiseaseorAttack']
    HvyAlcoholConsump=request.form['HvyAlcoholConsump']
    GenHlth=request.form['GenHlth']
    DiffWalk=request.form['DiffWalk']
    Sex=request.form['Sex']
    Age=request.form['Age']
    arr=np.array([[HighBP, HighChol, BMI, Smoker, Stroke, HeartDiseaseorAttack, HvyAlcoholConsump, GenHlth,
       DiffWalk, Sex, Age]])
    # arr=[int(x) for x in request.form.values()]
    # arr=[np.array(arr)]
    pred=model.predict(arr)
    return render_template('after.html', data=pred)

  
# @app.route('/predict2', methods=['POST'])
# def predict2():
#     model2=pickle.load(open(r'C:\Users\Kshitij\OneDrive\Desktop\edi\hdfinal.pkl','rb'))
#     Sex=request.form['Sex']
#     ExerciseAngina =request.form['ExerciseAngina']
#     Age =request.form['Age']
#     ChestPainType =request.form['ChestPainType']
#     FastingBS=request.form['FastingBS']
#     RestingECG =request.form['RestingECG']
#     ST_Slope=request.form['ST_Slope']
#     RestingBP=request.form['RestingBP']
#     Cholesterol=request.form['Cholesterol']
#     MaxHR=request.form['MaxHR']
#     Oldpeak=request.form['Oldpeak']
#     arr=np.array([[Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS,
#        RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope]])
#     # arr=[int(x) for x in request.form.values()]
#     # arr=[np.array(arr)]
#     pred=model2.predict(arr)
#     return render_template('after2.html', data=pred)   

if(__name__=="__main__"):
    app.run(debug=True)
