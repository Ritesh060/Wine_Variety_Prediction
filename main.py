from flask import Flask, render_template, request, jsonify, redirect
from keras.models import load_model
import numpy as np
import pandas as pd
from keras.preprocessing.text import Tokenizer
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
from keras_preprocessing.sequence import pad_sequences

app = Flask(__name__)
data = pd.read_csv('OSX_DS_assignment.csv')
model = load_model('Wine_Variety.h5', compile=False)
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data['variety'])
X_title = data['review_title']
X_desc = data['review_description']
X_winery = data['winery']
X_points = data['points']
num_classes = len(label_encoder.classes_)
y = to_categorical(y, num_classes=num_classes)
max_len = 100
tokenizer = Tokenizer()
tokenizer.fit_on_texts(np.concatenate((X_title, X_desc, X_winery)))

def preprocess_input(review_title, review_description, winery, points):
    X_title = tokenizer.texts_to_sequences([review_title])
    X_desc = tokenizer.texts_to_sequences([review_description])
    X_winery = tokenizer.texts_to_sequences([winery])
    max_len = 100
    X_title = pad_sequences(X_title, maxlen=max_len)
    X_desc = pad_sequences(X_desc, maxlen=max_len)
    X_winery = pad_sequences(X_winery, maxlen=max_len)
    points = np.array([points])
    return [X_title, X_desc, X_winery, points]


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    form_data = request.form.to_dict()
    review_title = form_data['review_title']
    review_description = form_data['review_description']
    winery = form_data['winery']
    points = int(form_data['points'])
    processed_input = preprocess_input(review_title, review_description, winery, points)
    prediction = model.predict(processed_input)
    predicted_class = label_encoder.inverse_transform([np.argmax(prediction)])[0]
    return render_template('result.html', prediction_text=predicted_class)     

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    review_title = data['review_title']
    review_description = data['review_description']
    winery = data['winery']
    points = data['points']
    processed_input = preprocess_input(review_title, review_description, winery, points)
    prediction = model.predict(processed_input)
    predicted_class = label_encoder.inverse_transform([np.argmax(prediction)])[0]
    return jsonify({'predicted_variety': predicted_class})



if __name__ == '__main__':
    app.run(debug=True)    