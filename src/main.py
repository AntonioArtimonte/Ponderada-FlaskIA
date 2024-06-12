from flask import Flask, request, jsonify, render_template
import time
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='keras')

modelo_normal = load_model('src/models/modelo_mnist.h5')
modelo_linear = load_model('src/models/linear_modelo_mnist.h5')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload_normal', methods=['POST'])
def upload_img_normal():
    file = request.files['file']
    
    img = Image.open(file)
    img = img.resize((28, 28))
    img = img.convert('L')
    img = np.array(img) / 255.0  
    img = img.reshape(1, 28, 28, 1) 

    start_time = time.time()
    predict_normal = modelo_normal.predict(img)
    end_time = time.time()
    predict_normal_time = end_time - start_time
    predict_normal = np.argmax(predict_normal, axis=1)[0] 

    return jsonify({
        'predict': int(predict_normal),
        'predict_normal_time': predict_normal_time
    })

@app.route('/upload_linear', methods=['POST'])
def upload_img_linear():
    file = request.files['file']
    
    img = Image.open(file)
    img = img.resize((28, 28))
    img = img.convert('L')
    img = np.array(img) / 255.0  
    img = img.reshape(1, 28, 28, 1) 

    start_time = time.time()
    predict_linear = modelo_linear.predict(img)
    end_time = time.time()
    predict_linear_time = end_time - start_time
    predict_linear = np.argmax(predict_linear, axis=1)[0]

    return jsonify({
        'predict_linear': int(predict_linear),
        'predict_linear_time': predict_linear_time
    })

if __name__ == '__main__':
    app.run(debug=True)
