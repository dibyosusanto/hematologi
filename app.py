from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)
app=Flask(__name__,template_folder='templates')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def index():
    if request.form['sex'] == 'l' :
    #Rujukan Nilai Haematocrit
        if float(request.form['txtHaematocrit']) > 52 :
            haematocrit = 2
        elif float(request.form['txtHaematocrit']) >= 40 :
            haematocrit = 1
        else :
            haematocrit = 0
       
       #Rujukan Nilai Haemoglobin
        if float(request.form['txtHaemoglobins']) > 18 :
            haemoglobins = 2
        elif float(request.form['txtHaemoglobins']) >= 13 :
            haemoglobins = 1
        else :
            haemoglobins = 0
     
       #Rujukan Nilai Erythrocyte
        if float(request.form['txtErythrocyte']) > 6.5 :
           erythrocyte = 2
        elif float(request.form['txtErythrocyte']) >= 4.5 :
            erythrocyte = 1
        else :
            erythrocyte = 0
       
       #Rujukan Nilai Leucocyte
        if float(request.form['txtLeucocyte']) > 10.6 :
            leucocyte = 2
        elif float(request.form['txtLeucocyte']) >= 3.8 :
            leucocyte = 1
        else :
            leucocyte = 0
     
       #Rujukan Nilai Thrombocyte
        if float(request.form['txtThrombocyte']) > 440 :
            thrombocyte = 2
        elif float(request.form['txtThrombocyte']) >= 150 :
            thrombocyte = 1
        else :
            thrombocyte = 0
    
       #Rujukan Nilai MCH
        if float(request.form['txtMch']) > 34 :
            mch = 2
        elif float(request.form['txtMch']) >= 26:
            mch = 1
        else : 
            mch = 0
     
       #Rujukan Nilai MCHC
        if float(request.form['txtMchc']) > 36 :
            mchc = 2
        elif float(request.form['txtMchc']) >= 32 :
            mchc = 1
        else :
            mchc = 0
       
       #Rujukan Nilai MCV
        if float(request.form['txtMcv']) > 100 :
            mcv = 2
        elif float(request.form['txtMcv']) >= 80 :
            mcv = 1
        else :
            mcv = 0
          
    elif request.form['sex'] == 'p' : 
    #Rujukan Nilai Haematocrit
        if float(request.form['txtHaematocrit']) > 47 :
            haematocrit = 2
        elif float(request.form['txtHaematocrit']) >= 35 :
            haematocrit = 1
        else :
            haematocrit = 0
        
        #Rujukan Nilai Haemoglobin
        if float(request.form['txtHaemoglobins']) > 16 :
            haemoglobins = 2
        elif float(request.form['txtHaemoglobins']) >= 12 :
            haemoglobins = 1
        else :
            haemoglobins = 0
      
        #Rujukan Nilai Erythrocyte
        if float(request.form['txtErythrocyte']) > 5.8 :
            erythrocyte = 2
        elif float(request.form['txtErythrocyte']) >= 3.6 :
            erythrocyte = 1
        else :
            erythrocyte = 0
        
        #Rujukan Nilai Leucocyte
        if float(request.form['txtLeucocyte']) > 10.6 :
            leucocyte = 2
        elif float(request.form['txtLeucocyte']) >= 3.8 :
            leucocyte = 1
        else :
            leucocyte = 0
    
        #Rujukan Nilai Thrombocyte
        if float(request.form['txtThrombocyte']) > 440 :
            thrombocyte = 2
        elif float(request.form['txtThrombocyte']) >= 150 :
            thrombocyte = 1
        else :
            thrombocyte = 0
      
        #Rujukan Nilai MCH
        if float(request.form['txtMch']) > 34 :
            mch = 2
        elif float(request.form['txtMch']) >= 26 :
            mch = 1
        else : 
            mch = 0
        
        #Rujukan Nilai MCHC
        if float(request.form['txtMchc']) > 36 :
            mchc = 2
        elif float(request.form['txtMchc']) >= 32 :
            mchc = 1
        else :
            mchc = 0
        
        #Rujukan Nilai MCV
        if float(request.form['txtMcv']) > 100 :
            mcv = 2
        elif float(request.form['txtMcv']) >= 80 :
            mcv = 1
        else :
            mcv = 0
    
    if request.form['sex'] == 'l' :
        arr = np.array([[haematocrit, haemoglobins, erythrocyte, leucocyte, thrombocyte, mch, mchc, mcv, 0, 1]])
        pred = model.predict(arr)
    else :
        arr = np.array([[haematocrit, haemoglobins, erythrocyte, leucocyte, thrombocyte, mch, mchc, mcv, 1, 0]])
        pred = model.predict(arr)
    return render_template('output.html', data=pred, haematocritVal=request.form['txtHaematocrit'], haemoglobinsVal=request.form['txtHaemoglobins'], erythrocyteVal=request.form['txtErythrocyte'], leucocyteVal=request.form['txtLeucocyte'], thrombocyteVal=request.form['txtThrombocyte'], mchVal=request.form['txtMch'], mchcVal=request.form['txtMchc'], mcvVal=request.form['txtMcv'], haematocrit=haematocrit, haemoglobins=haemoglobins, thrombocyte=thrombocyte, erythrocyte=erythrocyte, leucocyte=leucocyte, mcv=mcv, mch=mch, mchc=mchc)

if __name__ == "__main__":
    app.run(debug=True)