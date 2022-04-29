from flask import Flask, request, render_template
import numpy as np
import pickle, json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')    


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    
    global  __data_columns
    global __locations

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
        
    global __model
    with open('./artifacts/banglore_real_estate_model.pickle', 'rb') as f:
        __model = pickle.load(f)    
    
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[2] = total_sqft
    x[0] = bath
    x[1] = bhk
    if loc_index>=0:
        x[loc_index] = 1
        
    output = round(__model.predict([x])[0],2)

    return render_template('index.html', prediction_text='Estimated prediction of House price with following specification : Location :{} & SQFT : {} is Rs. {} Lakh'.format(location, total_sqft,output))






if __name__ == "__main__":
    app.run(debug=True)
